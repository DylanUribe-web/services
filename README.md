# CER Integration Services

**Proyecto:** Integración Zoho One ↔ AWS (Lambda, S3, API Gateway)  
**Autor / Líder técnico:** Dylan Uribe  
**Estado actual:** Sandbox funcional local, integración AWS pendiente  
**Objetivo:** Automatizar todo el ciclo del paciente desde lead hasta post-operatorio, garantizando trazabilidad, seguridad y experiencia boutique.

## Descripción General

Este repositorio contiene los servicios y Lambdas necesarios para simular y posteriormente implementar la integración entre **Zoho One (CRM, Flow, Forms, Sign)** y **AWS (Lambda, S3, API Gateway)**.

Las funciones permiten:

- Recibir datos de formularios y leads desde Zoho.
- Generar URLs presignadas para subir archivos a S3.
- Confirmar que los archivos se subieron correctamente.
- Procesar firmas digitales de documentos.
- Recibir callbacks del CRM y mantener trazabilidad con `traceId`.

Actualmente, todas las funciones pueden ejecutarse en **modo sandbox local** utilizando mocks y pruebas unitarias. La integración con AWS real se realizará cuando se configuren buckets y endpoints por parte de Ángel.

## Estructura del proyecto
```bash
services/
│   README.md                <- Este archivo
│   make_test.ps1            <- Script de pruebas
│   mock_server.py           <- Servidor mock para endpoints locales
│   poetry.lock
│   pyproject.toml
│   README dev-apply-steps.md <- Documentación de setup y progreso
│
├───crmCallback
├───fileConfirm
├───ingestForm
├───presignUpload
└───signHandler
```

## Descripcion de carpetas / Lambdas

| Carpeta         | Lambda        | Descripción                                                      |
| --------------- | ------------- | ---------------------------------------------------------------- |
| `crmCallback`   | crmCallback   | Recibe callbacks del CRM y registra eventos con `traceId`.       |
| `fileConfirm`   | fileConfirm   | Valida archivos en S3 por hash y tamaño; confirma su existencia. |
| `ingestForm`    | ingestForm    | Procesa formularios Zoho, normaliza datos y guarda JSON en S3.   |
| `presignUpload` | presignUpload | Genera URLs presignadas para subir archivos a S3 con SSE-KMS.    |
| `signHandler`   | signHandler   | Descarga PDFs firmados desde URL y los guarda en S3.             |

# Instalación y ejecución local

### Clonar repositorio desde CMD:

git clone https://github.com/DylanUribe-web/services
cd services


### Crear entorno y dependencias:

poetry install
poetry shell


### Ejecutar pruebas unitarias:

pytest -v


### Ejecutar servidor mock (opcional, para simular endpoints):

python mock_server.py


## Probar individualmente una Lambda:

from ingestForm.handler import handler

event = {"formData":{"leadId":"12345","brand":"FacialFillers","patientName":"juan perez"}}
context = {}
response = handler(event, context)
print(response)

## Documentación de cada Lambda

crmCallback/README.md

fileConfirm/README.md

ingestForm/README.md

presignUpload/README.md

signHandler/README.md

Cada README contiene: descripción, inputs/outputs, ejemplos de prueba local y pendientes de integración.

## Pruebas y Validación

Todas las Lambdas cuentan con pruebas unitarias usando pytest.

Mock server simula endpoints para pruebas end-to-end locales.

## Estado actual y pendientes

| Área                             | Estado        | Responsable    |
| -------------------------------- | ------------- | -------------- |
| Sandbox local                    | ✅ Funcional   | Dylan          |
| AWS S3 bucket y API Gateway      | ⏳ Pendiente   | Ángel          |
| Flow sandbox real                | ⏳ En espera   | Dylan / Ángel  |
| Logging y monitoreo centralizado | ⚙ Planificado | Dylan          |
| Integración Zoho Flow → CRM      | ⚙ Planificado | Dylan / Arturo |

## Notas

Todas las Lambdas generan traceId único para trazabilidad.

Se utiliza Server-Side Encryption KMS en S3 para cumplir con estándares de seguridad HIPAA-like.

El entorno actual permite desarrollo, pruebas y documentación mientras la infraestructura AWS real se configura.
