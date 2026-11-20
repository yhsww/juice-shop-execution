[CmdletBinding()]
param([switch]$SkipStart)

$ErrorActionPreference = 'Stop'
$ComposeFile = Join-Path $PSScriptRoot 'docker-compose.yml'

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    throw 'Docker CLI não encontrado. Instale e abra o Docker Desktop.'
}

& docker info *> $null
if ($LASTEXITCODE -ne 0) { throw 'Docker Engine não está disponível. Abra o Docker Desktop.' }

& docker compose -f $ComposeFile version
if ($LASTEXITCODE -ne 0) { throw 'Docker Compose v2 não está disponível.' }

if (-not $SkipStart) {
    & docker compose -f $ComposeFile pull
    if ($LASTEXITCODE -ne 0) { throw 'Falha ao baixar a imagem do Juice Shop.' }
    & docker compose -f $ComposeFile up -d
    if ($LASTEXITCODE -ne 0) { throw 'Falha ao iniciar o Juice Shop.' }
}

Write-Host 'Juice Shop configurado em http://localhost:3000' -ForegroundColor Green