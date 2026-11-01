# Clasificador de imágenes con ViT y Gradio

Aplicación local que permite cargar una imagen desde el navegador y obtener las
cinco clases más probables usando el modelo preentrenado
[`google/vit-base-patch16-224`](https://huggingface.co/google/vit-base-patch16-224).
El modelo clasifica imágenes según las categorías de ImageNet; no está entrenado
con un conjunto de datos propio.

## Requisitos

- Windows 10/11
- Python 3.10 a 3.12
- Conexión a Internet la primera vez que se inicia, para descargar el modelo

## Instalación en Windows (PowerShell)

Abrí PowerShell y ejecutá estos comandos para crear el directorio, entrar en él
y crear el entorno virtual:

```powershell
mkdir vit-gradio-classifier
cd vit-gradio-classifier
py -3.12 -m venv .venv
```

Activá el entorno virtual e instalá las dependencias:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

> Si PowerShell bloquea la activación del entorno, ejecutá
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` una vez
> y volvé a activar el entorno.

## Ejecución

Con el entorno virtual activo:

```powershell
python app.py
```

Abrí en el navegador la dirección local que muestra Gradio (normalmente
`http://127.0.0.1:7860`), cargá una imagen y consultá las predicciones. La
descarga inicial del modelo puede tardar; las siguientes ejecuciones reutilizan
la caché local de Hugging Face.

## Subir el proyecto a GitHub

El repositorio remoto del proyecto es
[`23923737/IFTS24`](https://github.com/23923737/IFTS24). Para subir los cambios
desde la carpeta del proyecto:

```powershell
git add .
git commit -m "Crear clasificador de imágenes con ViT y Gradio"
git push -u origin main
```

Para descargar el proyecto en otra computadora:

```powershell
git clone https://github.com/23923737/IFTS24.git
cd IFTS24
```

Git puede pedirte autenticarte con GitHub al hacer `push`; seguí el inicio de
sesión que ofrece Git Credential Manager. No compartas contraseñas ni tokens.
No subas `.venv`: está excluido por `.gitignore`. Para volver a trabajar,
abrí una terminal en la carpeta del proyecto y activá el entorno con
`.\.venv\Scripts\Activate.ps1`.
