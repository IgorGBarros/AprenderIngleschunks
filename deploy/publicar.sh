#!/usr/bin/env bash
# Gera o app e envia para a VPS (Linux, macOS ou WSL).
#
#   bash deploy/publicar.sh ubuntu@IP-DA-VPS
#
set -euo pipefail

SERVIDOR="${1:?uso: bash deploy/publicar.sh usuario@servidor}"
cd "$(dirname "$0")/../web"

echo "==> Gerando o app (npm run build)"
[[ -d node_modules ]] || npm ci
BASE_PATH=/ npm run build

echo "==> Enviando para $SERVIDOR"
rsync -az --delete dist/ "$SERVIDOR:/var/www/chunks/"
echo "==> Pronto! Abra o app no celular; ele atualiza sozinho."
