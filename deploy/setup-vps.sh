#!/usr/bin/env bash
# Prepara a VPS (Oracle Cloud, Ubuntu ou Oracle Linux) para hospedar o app Chunks
# de forma privada. Rode UMA vez, na VPS, dentro da pasta deploy/:
#
#   sudo bash setup-vps.sh tailscale                  # recomendado: só os seus aparelhos acessam
#   sudo bash setup-vps.sh domain chunks.seudominio.com igor   # domínio próprio + senha
#
# Opções (depois do modo):
#   --ollama                 instala o Ollama na própria VPS
#   --ollama-upstream IP:PORTA  usa um Ollama em outra máquina (ex.: o seu PC na Tailscale)
#
# Pode rodar de novo para trocar de modo ou de senha: ele só reescreve a configuração.

set -euo pipefail

usage() {
  sed -n '2,13p' "$0" | sed 's/^# \{0,1\}//'
  exit 1
}

[[ $EUID -eq 0 ]] || { echo "Rode com sudo: sudo bash $0 $*"; exit 1; }
cd "$(dirname "$0")"

MODE="${1:-}"; shift || true
DOMAIN=""; AUTH_USER=""
case "$MODE" in
  tailscale) ;;
  domain)
    DOMAIN="${1:-}"; AUTH_USER="${2:-}"
    [[ -n "$DOMAIN" && -n "$AUTH_USER" ]] || usage
    shift 2
    ;;
  *) usage ;;
esac

INSTALL_OLLAMA=0
OLLAMA_UPSTREAM="127.0.0.1:11434"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --ollama) INSTALL_OLLAMA=1 ;;
    --ollama-upstream) OLLAMA_UPSTREAM="${2:?informe IP:PORTA}"; shift ;;
    *) usage ;;
  esac
  shift
done

# Quem vai receber os arquivos do app (o usuário que chamou o sudo, ex.: ubuntu ou opc).
OWNER="${SUDO_USER:-root}"
WEB_ROOT=/var/www/chunks

step() { printf '\n\033[1;34m==> %s\033[0m\n' "$*"; }

# ------------------------------------------------------------------ Caddy
install_caddy() {
  command -v caddy >/dev/null && return
  step "Instalando o Caddy"
  if command -v apt-get >/dev/null; then
    apt-get update -q
    apt-get install -y -q debian-keyring debian-archive-keyring apt-transport-https curl gnupg
    curl -1sLf https://dl.cloudsmith.io/public/caddy/stable/gpg.key \
      | gpg --dearmor --yes -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
    curl -1sLf https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt \
      > /etc/apt/sources.list.d/caddy-stable.list
    apt-get update -q
    apt-get install -y -q caddy
  elif command -v dnf >/dev/null; then
    dnf install -y 'dnf-command(copr)'
    dnf copr enable -y @caddy/caddy
    dnf install -y caddy
  else
    echo "Sistema não suportado: instale o Caddy manualmente (https://caddyserver.com/docs/install)."
    exit 1
  fi
}

# ---------------------------------------------- firewall da Oracle (modo domínio)
# As imagens da Oracle bloqueiam tudo além da porta 22 no próprio sistema, além
# da Security List do painel (essa você abre no site, ver deploy/README.md).
open_web_ports() {
  step "Liberando as portas 80 e 443 no firewall da VPS"
  if command -v firewall-cmd >/dev/null && systemctl is-active -q firewalld; then
    firewall-cmd --permanent --add-service=http --add-service=https
    firewall-cmd --reload
  elif command -v iptables >/dev/null; then
    for port in 80 443; do
      iptables -C INPUT -p tcp --dport "$port" -m state --state NEW -j ACCEPT 2>/dev/null \
        || iptables -I INPUT -p tcp --dport "$port" -m state --state NEW -j ACCEPT
    done
    if command -v netfilter-persistent >/dev/null; then
      netfilter-persistent save
    else
      echo "Aviso: instale 'iptables-persistent' para as regras sobreviverem ao reboot."
    fi
  fi
}

# --------------------------------------------------------------- Tailscale
setup_tailscale() {
  if ! command -v tailscale >/dev/null; then
    step "Instalando a Tailscale"
    curl -fsSL https://tailscale.com/install.sh | sh
  fi
  if ! tailscale status >/dev/null 2>&1; then
    step "Conecte a VPS à sua conta Tailscale (abra o link que aparecer)"
    tailscale up
  fi
  step "Publicando o app só na sua rede Tailscale (HTTPS)"
  # Se o HTTPS ainda não estiver ativo na sua conta, o comando mostra um link para ativar.
  tailscale serve --bg 8080
}

# ------------------------------------------------------------------ Ollama
setup_ollama() {
  if ! command -v ollama >/dev/null; then
    step "Instalando o Ollama"
    curl -fsSL https://ollama.com/install.sh | sh
  fi
  echo "Baixe um modelo, por exemplo: ollama pull qwen2.5:7b"
}

# ------------------------------------------------------------- configuração
write_caddy_config() {
  step "Configurando o Caddy"
  sed "s|__OLLAMA__|$OLLAMA_UPSTREAM|" chunks.caddy > /etc/caddy/chunks.caddy

  if [[ "$MODE" == tailscale ]]; then
    cp Caddyfile.tailscale /etc/caddy/Caddyfile
  else
    local pass pass2 hash
    while true; do
      read -rsp "Senha para o usuário $AUTH_USER: " pass; echo
      read -rsp "Repita a senha: " pass2; echo
      [[ -n "$pass" && "$pass" == "$pass2" ]] && break
      echo "As senhas não conferem (ou estão vazias). Tente de novo."
    done
    hash="$(caddy hash-password --plaintext "$pass")"
    sed -e "s|__DOMAIN__|$DOMAIN|" -e "s|__USER__|$AUTH_USER|" -e "s|__HASH__|$hash|" \
      Caddyfile.domain > /etc/caddy/Caddyfile
  fi

  caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
  systemctl enable -q caddy
  systemctl reload-or-restart caddy
}

prepare_web_root() {
  mkdir -p "$WEB_ROOT"
  if [[ ! -f "$WEB_ROOT/index.html" ]]; then
    echo '<!doctype html><meta charset="utf-8"><p>Chunks: falta enviar o app (deploy/README.md, passo 3).</p>' \
      > "$WEB_ROOT/index.html"
  fi
  chown -R "$OWNER:$OWNER" "$WEB_ROOT"
  chmod 755 "$WEB_ROOT"
}

install_caddy
prepare_web_root
[[ $INSTALL_OLLAMA -eq 1 ]] && setup_ollama
[[ "$MODE" == domain ]] && open_web_ports
write_caddy_config
[[ "$MODE" == tailscale ]] && setup_tailscale

step "Pronto!"
if [[ "$MODE" == tailscale ]]; then
  tailscale serve status || true
  echo "Abra o endereço https://....ts.net acima no celular (com o app Tailscale ligado)."
else
  echo "Abra https://$DOMAIN no celular e entre com o usuário $AUTH_USER."
fi
echo "Os arquivos do app ficam em $WEB_ROOT (dono: $OWNER)."
