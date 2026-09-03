from fastapi import FastAPI
from fastapi.responses import FileResponse
import random
import os

app = FastAPI()


@app.get("/obtener_cedula")
def obtener_cedula():
    """Devuelve un número entero aleatorio de 10 dígitos bajo la clave 'cedula'."""
    numero = random.randint(10**9, 10**10 - 1)
    return {"cedula": numero}


@app.get("/swagger.html")
def swagger_static():
    """Sirve el archivo swagger.html desde la raíz del proyecto."""
    file_path = os.path.join(os.getcwd(), 'swagger.html')
    if not os.path.exists(file_path):
        return {"error": "swagger.html no encontrado en la raíz del proyecto"}
    return FileResponse(file_path, media_type='text/html')
