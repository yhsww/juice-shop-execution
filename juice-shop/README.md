# OWASP Juice Shop — ambiente local com Docker

Este diretório incorpora os arquivos do repositório `yhsww/juice-shop`, usado para preparar e executar a aplicação sob teste.

Imagem fixada: `bkimminich/juice-shop:v20.3.0`.

## Inicialização

Na raiz de `juice-shop-execution`, use:

```powershell
python run.py --start-app --scenario CEN-IDT-01
python run.py --start-app --all
```

Ou inicie/pare manualmente:

```powershell
docker compose -f juice-shop/docker-compose.yml up -d
docker compose -f juice-shop/docker-compose.yml down
```

A porta é publicada apenas em `127.0.0.1:3000`. O Juice Shop é intencionalmente vulnerável; mantenha-o restrito ao ambiente local/ autorizado.

Repositório de origem: https://github.com/yhsww/juice-shop