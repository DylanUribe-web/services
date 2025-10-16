# ============================
# make_test_clean.ps1
# ============================

# 1️⃣ Limpiar todos los __pycache__ del proyecto
Write-Host "🧹 Limpiando __pycache__..."
Get-ChildItem -Path . -Recurse -Include "__pycache__" | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

# 2️⃣ Configurar PYTHONPATH al directorio actual
Write-Host "🛠 Configurando PYTHONPATH..."
$env:PYTHONPATH = "$PWD"

# 3️⃣ Ejecutar pytest con detalles y sin warnings
Write-Host "🚀 Corriendo pytest..."
poetry run pytest -v --disable-warnings --maxfail=5
