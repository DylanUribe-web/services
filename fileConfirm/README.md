# fileConfirm Lambda

## Descripción
Confirma que un archivo subido a S3 exista y cumpla con hash SHA256 y tamaño esperado.  
Publica un evento (simulado por print) indicando la confirmación.

## Entradas esperadas (event)
```json
{
  "leadId": "12345",
  "s3Key": "forms/brand/2025/10/12345/form.json",
  "sha256": "abcdef123456...",
  "size": 12345,
  "eTag": "etag"
}

## Salida
{
  "statusCode": 200,
  "body": {
    "traceId": "20251020123000-uuid"
  }
}

## Cómo probar local

Simular un archivo en S3 (mock o bucket de prueba).

Ejecutar:
from handler import handler

event = {
    "leadId":"12345",
    "s3Key":"forms/test/form.json",
    "sha256":"<hash>",
    "size":123
}
context = {}
response = handler(event, context)
print(response)

## Pendientes

Conectar con eventos reales desde presigned URL.

Mejor manejo de logs y errores.

Integración con Flow / CRM.