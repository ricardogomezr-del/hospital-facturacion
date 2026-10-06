# Facturacion

Microservicio académico para la práctica de API Gateway.

## Endpoint principal
`/facturas`

## Render
Build Command:
`pip install -r requirements.txt`

Start Command:
`gunicorn app:app`

## Endpoints
- GET `/`
- GET `/health`
- GET `/facturas`
- GET `/facturas/<id>`
- POST `/facturas`

Los datos se almacenan en memoria y se reinician cuando el servicio vuelve a desplegarse o reinicia.
