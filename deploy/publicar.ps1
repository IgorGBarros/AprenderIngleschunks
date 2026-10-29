# Gera o app e envia para a VPS (Windows / PowerShell).
#
#   .\deploy\publicar.ps1 -Servidor ubuntu@IP-DA-VPS
#   .\deploy\publicar.ps1 -Servidor ubuntu@minha-vps      # nome da máquina na Tailscale
#
# Precisa do Node.js (npm) e do OpenSSH (já vem no Windows 10/11).

param(
    [Parameter(Mandatory = $true)][string]$Servidor,
    [string]$Chave = ""
)

$ErrorActionPreference = "Stop"
$raiz = Split-Path -Parent $PSScriptRoot
$sshArgs = @()
if ($Chave) { $sshArgs = @("-i", $Chave) }

Push-Location (Join-Path $raiz "web")
try {
    Write-Host "==> Gerando o app (npm run build)" -ForegroundColor Cyan
    if (-not (Test-Path "node_modules")) { npm ci; if ($LASTEXITCODE) { throw "npm ci falhou" } }
    $env:BASE_PATH = "/"
    npm run build
    if ($LASTEXITCODE) { throw "npm run build falhou" }

    Write-Host "==> Enviando para $Servidor" -ForegroundColor Cyan
    ssh @sshArgs $Servidor "rm -rf /tmp/chunks-dist"
    if ($LASTEXITCODE) { throw "Não consegui conectar em $Servidor" }
    scp @sshArgs -r -q dist "${Servidor}:/tmp/chunks-dist"
    if ($LASTEXITCODE) { throw "scp falhou" }
    # Troca os arquivos de uma vez: o app nunca fica pela metade.
    ssh @sshArgs $Servidor "rm -rf /var/www/chunks/* && cp -r /tmp/chunks-dist/. /var/www/chunks/ && rm -rf /tmp/chunks-dist"
    if ($LASTEXITCODE) { throw "Falhou ao copiar para /var/www/chunks (rodou o setup-vps.sh?)" }

    Write-Host "==> Pronto! Abra o app no celular; ele atualiza sozinho." -ForegroundColor Green
}
finally {
    Remove-Item Env:BASE_PATH -ErrorAction SilentlyContinue
    Pop-Location
}
