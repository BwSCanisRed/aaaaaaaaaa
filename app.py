from random import randint

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Servicio de cédula",
    description="API para obtener un número entero aleatorio de 10 dígitos y su equivalente romano.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
)


def to_roman(number: int) -> str:
    """Convierte un número entero a número romano."""
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    result = ""
    for value, numeral in zip(values, numerals):
        while number >= value:
            result += numeral
            number -= value
    return result


@app.get("/swagger", include_in_schema=False)
async def swagger_html() -> HTMLResponse:
    """Devuelve una página HTML con Swagger UI."""
    return HTMLResponse(
        """
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Swagger - Servicio de cédula</title>
            <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@5.11.0/swagger-ui.css" />
            <style>
                html { box-sizing: border-box; overflow: -moz-scrollbars-vertical; overflow-y: scroll; }
                *, *:before, *:after { box-sizing: inherit; }
                body { margin: 0; background: #f5f5f5; }
                #swagger-ui { max-width: 1200px; margin: 20px auto; }
            </style>
        </head>
        <body>
            <div id="swagger-ui"></div>
            <script src="https://unpkg.com/swagger-ui-dist@5.11.0/swagger-ui-bundle.js"></script>
            <script>
                window.onload = function () {
                    SwaggerUIBundle({
                        url: '/openapi.json',
                        dom_id: '#swagger-ui',
                        deepLinking: true,
                        presets: [
                            SwaggerUIBundle.presets.apis,
                            SwaggerUIBundle.SwaggerUIStandalonePreset
                        ],
                        layout: "BaseLayout",
                        theme: "agate"
                    });
                };
            </script>
        </body>
        </html>
        """
    )


@app.get("/obtener_cedula")
def obtener_cedula() -> int:
    """Devuelve un número entero aleatorio de 10 dígitos."""
    return randint(10**9, 10**10 - 1)


@app.get("/obtener_numero_romano")
def obtener_numero_romano() -> str:
    """Devuelve un número romano aleatorio entre 50 y 100."""
    numero = randint(50, 100)
    return to_roman(numero)