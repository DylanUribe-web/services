# crmCallback Lambda

## Descripción
Lambda que recibe actualizaciones del CRM (Zoho) y registra la información para trazabilidad.  
Actualmente el logger es básico (`get_logger`) y funciona en modo `dev`. Se puede mejorar luego para integrar alertas o logs estructurados en CloudWatch.

## Flujo
- Invocado desde Zoho Flow o CRM callback.
- Genera un `traceId` único para cada evento.
- Loguea evento completo.
- Retorna estado 200 OK.

## Entradas esperadas (event)
```json
{
  "dealId": "12345",
  "status": "Surgery Scheduled",
  "assignedTo": "coordinator@example.com"
}

## Salida
{
  "statusCode": 200,
  "body": "{\"message\":\"ok\"}"
}

## Como probar localmente
from handler import handler

event = {"dealId":"12345","status":"Surgery Scheduled"}
context = {}
response = handler(event, context)
print(response)

## Pendientes / Mejoras

Logger avanzado con CloudWatch o DynamoDB.

Validación de payload.

Manejo de errores más detallado.