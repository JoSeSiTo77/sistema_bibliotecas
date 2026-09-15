# Sistema de Gestión de Biblioteca SENA CTM

## Descripción

Aplicación de consola en Python para administrar una biblioteca. Incluye autenticación por documento y contraseña, roles Administrador, Aprendiz e Instructor, gestión de usuarios, libros y ejemplares, consulta de catálogo y disponibilidad, préstamos, devoluciones e historial. También calcula sanciones por mora y ofrece reportes y un resumen general.

Los datos se conservan en archivos CSV y las contraseñas se protegen con bcrypt. El usuario inicial es **root**, documento **1**, contraseña **admin123**.

## Instalación

Con Python instalado en Windows, abre PowerShell en la raíz del proyecto y pega:

```powershell
$ErrorActionPreference = "Stop"
if (-not (Test-Path ".venv")) {
    py -m venv .venv
    if ($LASTEXITCODE -ne 0) { throw "No se pudo crear .venv." }
}
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) { throw "No se pudo actualizar pip." }
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) { throw "No se pudieron instalar las dependencias." }
```

Para iniciar: `.venv\Scripts\python.exe main.py`.

## Crear ejecutable de Windows

Después de instalar, ejecuta este bloque desde la raíz del proyecto. Empaqueta los cuatro CSV actuales como datos iniciales y utiliza `assets/biblioteca.ico` como icono. PyInstaller se instala solo como herramienta de construcción.

```powershell
$ErrorActionPreference = "Stop"
foreach ($archivo in @("main.py", "assets/biblioteca.ico", ".venv/Scripts/python.exe",
                      "data/usuarios.csv", "data/libros.csv", "data/ejemplares.csv", "data/prestamos.csv")) {
    if (-not (Test-Path $archivo -PathType Leaf)) { throw "Falta el archivo: $archivo" }
}
& .\.venv\Scripts\python.exe -m pip install PyInstaller
if ($LASTEXITCODE -ne 0) { throw "No se pudo instalar PyInstaller." }
foreach ($carpeta in @("build", "dist")) {
    if (Test-Path $carpeta) { Remove-Item $carpeta -Recurse -Force }
}
& .\.venv\Scripts\python.exe -m PyInstaller --noconfirm --onefile --console --name BibliotecaSENA --icon assets/biblioteca.ico --add-data "assets/biblioteca.ico:assets" --add-data "data/usuarios.csv:data" --add-data "data/libros.csv:data" --add-data "data/ejemplares.csv:data" --add-data "data/prestamos.csv:data" main.py
if ($LASTEXITCODE -ne 0) { throw "No se pudo generar el ejecutable." }
$escritorio = Join-Path $env:USERPROFILE "Desktop"
New-Item -ItemType Directory -Path $escritorio -Force | Out-Null
Copy-Item "dist/BibliotecaSENA.exe" (Join-Path $escritorio "BibliotecaSENA.exe") -Force
Write-Host "Creado: $escritorio\BibliotecaSENA.exe"
```

Al abrir `BibliotecaSENA.exe`, se crea `data/` junto al ejecutable y se copian únicamente los CSV que falten. Los cambios se conservan entre ejecuciones; los archivos existentes no se reemplazan. Mantén el ejecutable en una carpeta con permiso de escritura.
