# Dev Apply Steps

1. Configurar AWS CLI y perfil:
   ```powershell
   aws configure --profile dev
   $env:AWS_PROFILE="dev"

2. Inicializar Terraform:
    cd infrastructure/envs/dev
    terraform init
    terraform validate

3. Aplicar IAM:
    terraform plan -out=iam.plan
    terraform apply "iam.plan"

 4. Aplicar resto de módulos:
    terraform plan -out=full.plan
    terraform apply "full.plan"

5. Revisar outputs:

    * Lambda role ARN
    * Deploy role ARN
    * Audit role ARN
    * API Shared Key ARN

6. Ejecutar tests unitarios:
    cd services
    poetry run pytest -q

7. Ejecutar tests y eliminacion de Pycache
    cd services
    .\make_test.ps1