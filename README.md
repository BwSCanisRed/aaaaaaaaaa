
# Servicio FastAPI: obtener_cedula

Este proyecto expone un endpoint `GET /obtener_cedula` que devuelve un número entero aleatorio de 10 dígitos en formato JSON.

- Contenido del repositorio:
- `app.py`: aplicación FastAPI (único archivo de la app)
- `requirements.txt`: dependencias
- `Dockerfile`, `docker-compose.yml`: archivos para ejecutar en Docker
- `postman_collection.json`: colección Postman para importar
- `requirements.txt`: dependencias
- `Dockerfile`, `docker-compose.yml`: archivos para ejecutar en Docker
- `postman_collection.json`: colección Postman para importar

Respuesta / Payload
--------------------
Endpoint:

- `GET /obtener_cedula`

Ejemplo de respuesta (JSON):

```json
{ "cedula": 1234567890 }
```

Cómo ejecutar (sin Docker)
--------------------------

1. Crear y activar un entorno virtual (recomendado):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Iniciar servidor de desarrollo:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

El endpoint quedará disponible en `http://127.0.0.1:8000/obtener_cedula` y la documentación interactiva en `http://127.0.0.1:8000/docs`.

Cómo ejecutar con Docker
------------------------

Requisitos: Docker Desktop instalado y corriendo.

Desde la raíz del proyecto (`c:\Users\CSI\Desktop\TALLERDOCKER`) ejecuta: 

```powershell
docker compose up --build -d
```

Comandos útiles:

```powershell
docker compose ps
docker compose logs -f
docker compose down
```

Después de levantar el servicio con Docker, el endpoint estará en `http://127.0.0.1:8000/obtener_cedula`.

Problemas comunes
-----------------
- Si `docker` no se reconoce: asegúrate de que Docker Desktop esté instalado y en ejecución, y reinicia la terminal.
- Si el puerto `8000` está ocupado, cámbialo en `docker-compose.yml` y en la URL que uses.

Colección Postman
-----------------
Importa el archivo `postman_collection.json` en Postman (File → Import → selecciona `postman_collection.json`). La colección contiene una petición `GET /obtener_cedula` con la variable `base_url` por defecto en `http://127.0.0.1:8000`.

Ejemplo rápido usando `curl`:

```bash
curl http://127.0.0.1:8000/obtener_cedula
```

**Despliegue continuo en Render (GitHub Actions)**

Este repositorio incluye un workflow de GitHub Actions (`.github/workflows/deploy_to_render.yml`) que dispara un despliegue en Render cada vez que se hace push a la rama `main`.

Requisitos en Render:
- Crea una cuenta en https://render.com y añade un nuevo **Web Service**. Selecciona desplegar desde GitHub y configura el servicio para usar el `Dockerfile` del repositorio (o usar el entorno de Python si lo prefieres).
- Copia el **Service ID** del servicio (lo necesitas para la API).
- Genera una API key en Render (Dashboard → Account → API Keys).

Configura secrets en tu repositorio GitHub:
- `RENDER_API_KEY` — tu API key de Render
- `RENDER_SERVICE_ID` — el Service ID de tu Web Service en Render

El workflow hace lo siguiente:
1. En push a `main`, crea un deploy mediante la API de Render (`POST /v1/services/{service_id}/deploys`).
2. Obtiene el `deploy_id` y hace polling consultando el estado del deploy hasta que el despliegue esté `active` o falle.

Para activar el despliegue continuo:
1. Sube tus cambios y haz push a `main`.
2. En GitHub Actions verás el job `Deploy to Render` que activará el deploy en Render.

Notas:
- Asegúrate de que `RENDER_API_KEY` y `RENDER_SERVICE_ID` estén configurados en `Settings → Secrets and variables → Actions` del repositorio.
- Si prefieres, puedes conectar Render directamente con el repositorio desde su panel y usar la integración visual en lugar del trigger por API.

