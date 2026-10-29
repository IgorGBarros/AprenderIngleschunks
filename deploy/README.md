# App no celular, hospedado na sua VPS (privado)

O app web já é um **PWA**: depois de aberto uma vez pelo navegador, ele é
instalado na tela inicial e abre como um aplicativo. Tem ícone próprio, abre
em tela cheia e funciona offline. Não precisa de loja nem de APK.

Esta pasta coloca o app na sua VPS da Oracle sem deixá-lo público.

| Arquivo | Para quê |
|---|---|
| `setup-vps.sh` | Roda uma vez na VPS: instala o Caddy e configura o acesso privado. |
| `publicar.ps1` | No seu PC com Windows: gera o app e envia para a VPS. |
| `publicar.sh` | O mesmo, para Linux, macOS ou WSL. |
| `chunks.caddy`, `Caddyfile.*` | Configuração do servidor (o `setup-vps.sh` usa estes arquivos). |

## Escolha como deixar privado

**A) Tailscale (recomendado).** Uma rede privada entre os seus aparelhos. O
app não fica na internet: só abre no celular ou no PC que estiverem logados
na sua conta Tailscale.

- Não precisa abrir portas na Oracle nem ter domínio.
- O HTTPS vem pronto, o que o microfone e a instalação do app exigem.
- Funciona igual no Android e no iPhone.
- Custo: instalar o app Tailscale no celular (grátis) e deixá-lo ligado.

**B) Domínio próprio com senha.** O endereço `https://chunks.seudominio.com`
fica na internet, mas tudo pede usuário e senha. Os buscadores ficam
bloqueados.

- Não precisa de nada instalado no celular.
- Precisa de um domínio e de abrir as portas 80 e 443 na Oracle.
- No iPhone, o app instalado às vezes volta a pedir a senha.

Se estiver em dúvida, use a **A**.

## 1. Envie esta pasta para a VPS

No PowerShell do seu PC, dentro da pasta do projeto, troque o IP pelo da sua
VPS. O usuário padrão é `ubuntu` no Ubuntu e `opc` no Oracle Linux.

```powershell
scp -r deploy ubuntu@IP-DA-VPS:~/chunks-deploy
ssh ubuntu@IP-DA-VPS
```

## 2. Rode o setup na VPS

### Opção A: Tailscale

1. Crie uma conta em https://tailscale.com (dá para entrar com Google ou GitHub).
2. No painel da Tailscale, ative o HTTPS: **DNS › HTTPS Certificates ›
   Enable**. Se a opção não aparecer, ative antes o **MagicDNS**, na mesma
   página.
3. Na VPS, rode:

   ```bash
   sudo bash ~/chunks-deploy/setup-vps.sh tailscale
   ```

   O script mostra um link para conectar a VPS à sua conta. Abra o link e
   aprove. No fim, ele mostra o endereço do app, algo como
   `https://nome-da-vps.tail1234.ts.net`.
4. No celular, instale o app **Tailscale** (Play Store ou App Store) e entre
   com a mesma conta.

### Opção B: domínio + senha

1. No seu provedor de DNS, crie um registro **A** apontando
   `chunks.seudominio.com` para o IP público da VPS.
2. No painel da Oracle, libere as portas 80 e 443: **Networking › Virtual
   Cloud Networks › (sua VCN) › Security Lists › Default › Add Ingress
   Rules**. Use Source `0.0.0.0/0`, protocolo TCP e portas `80,443`.
3. Na VPS, rode:

   ```bash
   sudo bash ~/chunks-deploy/setup-vps.sh domain chunks.seudominio.com igor
   ```

   O script pede a senha e libera as portas também no firewall interno da VPS.
   As imagens da Oracle bloqueiam essas portas por padrão. O certificado HTTPS
   é emitido sozinho.

Para trocar a senha ou mudar de modo, é só rodar o script de novo.

## 3. Envie o app

Escolha uma das três formas:

- **Pelo PC com Windows:** no PowerShell, na pasta do projeto, rode o comando
  abaixo. Na opção A, você pode usar o nome da VPS na Tailscale no lugar do IP.

  ```powershell
  .\deploy\publicar.ps1 -Servidor ubuntu@IP-DA-VPS
  ```

  Se o PowerShell bloquear o script, rode antes:
  `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
- **Por Linux, macOS ou WSL:**

  ```bash
  bash deploy/publicar.sh ubuntu@IP-DA-VPS
  ```
- **Automático pelo GitHub:** a cada push na `main`, o workflow
  `.github/workflows/web.yml` testa, gera e envia o app para a VPS. Para
  ligar:
  1. Na VPS, crie uma chave só para o GitHub:

     ```bash
     ssh-keygen -t ed25519 -f ~/.ssh/github_deploy -N "" -C github-actions
     cat ~/.ssh/github_deploy.pub >> ~/.ssh/authorized_keys
     cat ~/.ssh/github_deploy        # copie tudo, incluindo as linhas BEGIN/END
     ```
  2. No GitHub, vá em **Settings › Secrets and variables › Actions** e crie:
     - o secret `VPS_SSH_KEY`, com a chave copiada acima;
     - a variável `VPS_HOST`, com o IP público da VPS (a porta 22 da Oracle
       já vem aberta);
     - a variável `VPS_USER`, só se o seu usuário não for `ubuntu` (por
       exemplo, `opc`).
  3. Para publicar na hora, sem esperar um push, use **Actions › Web app ›
     Run workflow**.

> **GitHub Pages agora fica desligado.** Ele é público, então o workflow só
> publica lá se você criar a variável `GITHUB_PAGES` com o valor `true`.

## 4. Instale no celular

Abra o endereço do app no celular:

- **Android (Chrome):** toque no menu ⋮ e depois em **Instalar app** (ou
  "Adicionar à tela inicial").
- **iPhone (Safari):** toque em Compartilhar e depois em **Adicionar à Tela
  de Início**.

Pronto: o ícone **Chunks** aparece com os outros apps. Para atualizar, publique
de novo (passo 3); o app pega a versão nova na próxima vez que abrir com
internet.

O seu progresso e os seus chunks ficam salvos **no próprio celular**. O
servidor só entrega os arquivos do app; ele não guarda nenhum dado seu.

## Ollama (gerar entrevistas pelo celular)

O app chama o Ollama no mesmo endereço, em `https://.../ollama`, e o Caddy
repassa o pedido para o Ollama. Em *+ Nova vaga › Configurar Ollama*, o
endereço já vem preenchido assim. Você escolhe onde o Ollama roda:

- **Na VPS (recomendado na VPS grátis ARM, 24 GB de RAM e 200 GB de disco):**
  rode o setup com `--ollama`. Ele instala o Ollama, baixa o modelo e deixa o
  modelo carregado na memória por 1 hora, para os próximos pedidos saírem mais
  rápido. O Ollama só escuta dentro da VPS: quem chega até ele é o Caddy, que já
  está protegido (Tailscale ou senha).

  ```bash
  sudo bash ~/chunks-deploy/setup-vps.sh tailscale --ollama
  ```

  Escolha o modelo com `--modelo`. Para trocar depois, rode
  `ollama pull NOME` na VPS e escolha o modelo em *Configurar Ollama* no app.

  | Modelo | Tamanho | Na VPS (4 CPUs ARM, sem placa de vídeo) |
  |---|---|---|
  | `qwen2.5:3b` | ~2 GB | O mais rápido. Às vezes erra o formato; é só gerar de novo. |
  | `qwen2.5:7b` (padrão) | ~5 GB | Bom equilíbrio. Uma entrevista leva alguns minutos. |
  | `qwen2.5:14b` | ~9 GB | Respostas melhores, mas cerca de 2x mais lento que o 7b. |

  Os 24 GB de RAM e os 200 GB de disco cabem com folga em qualquer um deles,
  até em vários ao mesmo tempo. O gargalo é a CPU. Confira no painel da Oracle
  se a VPS está com as **4 OCPUs** do plano grátis: com menos, fica
  proporcionalmente mais lento. Enquanto gera, o app mostra o progresso etapa
  por etapa; pode deixar a tela aberta.
- **No seu PC (opção A, se ele tiver placa de vídeo):** o PC faz o trabalho pesado e a VPS só repassa o
  pedido.
  1. Instale a Tailscale no PC.
  2. No PC, faça o Ollama aceitar conexões da rede. No Windows, crie a
     variável de ambiente `OLLAMA_HOST` com o valor `0.0.0.0` (*Editar as
     variáveis de ambiente do sistema*). Depois feche o Ollama no ícone da
     bandeja e abra de novo. Se o Firewall do Windows perguntar, permita.
  3. Na VPS, aponte para o IP do PC na Tailscale (`tailscale ip` no PC; começa
     com `100.`):

     ```bash
     sudo bash ~/chunks-deploy/setup-vps.sh tailscale --ollama-upstream 100.x.y.z:11434
     ```

  O PC precisa estar ligado na hora de gerar. Estudar não precisa: o resto do
  app funciona sem ele.

## Problemas comuns

| Sintoma | Causa provável |
|---|---|
| A página não abre (opção A) | O Tailscale do celular está desligado. |
| A página não abre (opção B) | Falta a regra da Security List na Oracle, ou o DNS ainda não propagou. Veja o log com `sudo journalctl -u caddy -n 50`. |
| "Falta enviar o app" | O setup rodou, mas o passo 3 ainda não. |
| O microfone não funciona | O app tem que abrir em `https://`. Pelo IP direto (`http://`) o navegador bloqueia. |
| O Ollama dá erro 502 | O Ollama não está rodando no destino. Na VPS, confira com `systemctl status ollama`; no PC, veja se o `ollama serve` está aberto. |
| Mudei algo e não aparece | Feche o app por completo e abra de novo (com internet). |
