
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

