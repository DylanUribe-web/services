# Services Repository

Este repositorio contiene los distintos Lambdas del proyecto:

- `ingestForm`
- `presignUpload`
- `signHandler`
- `crmCallback`

## Logging & Trace

- Cada Lambda debe registrar un `traceId` con el formato: `{timestamp}-{uuid4()}`.
- Todos los logs deben incluir `LambdaName` y `Stage` (dev/prod).
- Esto permite correlacionar logs y seguir trazabilidad de requests entre Lambdas.
