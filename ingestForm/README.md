# ingestForm Lambda

## Descripción
Recibe datos de formularios Zoho, valida el payload y lo guarda en S3 bajo ruta estructurada.

## Entradas esperadas (event)
```json
{
  "formData": {
    "leadId": "12345",
    "brand": "FacialFillers",
    "patientName": "Juan Perez",
    "fields": {...}
  }
}

## Salida
{
  "statusCode": 200,
  "body": {
    "s3Key": "forms/FacialFillers/2025/10/12345/form.json",
    "traceId": "20251020123000-uuid"
  }
}

## Como probar localmente
from handler import handler

event = {
  "formData": {"leadId":"12345","brand":"FacialFillers","patientName":"juan perez"}
}
context = {}
response = handler(event, context)
print(response)

## Pendientes
Pendientes

Integración con API Gateway real.

Mejor manejo de errores y validaciones.

Logging centralizado.