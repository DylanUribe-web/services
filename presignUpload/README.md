# presignUpload Lambda

## Descripción
Genera URLs presignadas para subir archivos a S3 de manera segura con SSE-KMS.

## Entradas esperadas (event)
```json
{
  "leadId": "12345",
  "fileName": "lip_before.jpg",
  "contentType": "image/jpeg"
}

## Salida
{
  "statusCode": 200,
  "body": {
    "url": "https://s3.amazonaws.com/...",
    "s3Key": "files/12345/2025/10/lip_before.jpg",
    "traceId": "20251020123000-uuid"
  }
}

## Cómo probar local

Simular event dict con leadId y fileName.

Ejecutar handler.

## Pendientes

Conectar con Flow.

Limitar expiración de URLs según políticas.

Logging centralizado.