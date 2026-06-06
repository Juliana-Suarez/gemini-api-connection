import os
from google import genai
from dotenv import load_dotenv


# Cargar variables entorno desde el archivo
load_dotenv()

clave_api= os.getenv("GEMINI_API_KEY")

cliente = genai.Client(api_key=clave_api)


def ejecutar_consulta():
    print("Ejecutar consulta....")

    try:
        respuesta = cliente.models.generate_content(
            model= "gemini-3.5-flash",
            contents = "Presentate como experto en ML y responde a esta pregunta " \
            ":¿Cuales son las mejores practicas para procesamiento de datos? "
        )
        print("Respuesta de Gemini:")
        print(respuesta.text)
    except Exception as e: 
        print("Error al ejecutar", e)

if __name__ == "__main__":
    ejecutar_consulta() 