# signHandler Lambda

## Descripción
Descarga PDFs firmados desde URL, los guarda en S3 bajo ruta organizada por brand y dealId.

## Entradas esperadas (event)
```json
{
  "dealId": "12345",
  "brand": "FacialFillers",
  "downloadUrl": "https://signed-docs.com/12345.pdf"
}

## Salida
{
  "statusCode": 200,
  "body": {
    "s3Key": "sign/FacialFillers/2025/10/12345/signed.pdf",
    "traceId": "20251020123000-uuid"
  }
}

## Cómo probar local

Simular URL con PDF accesible.

Ejecutar handler.

## Pendientes

Actualizar DynamoDB temporal o tabla de tracking.

Manejo de errores más robusto (descarga fallida, archivo corrupto).

Integración Flow ↔ CRM.