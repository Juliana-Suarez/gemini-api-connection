# Conexión a la API de Gemini (Python)

Este repositorio contiene un script en Python diseñado para conectarse a la API de Gemini utilizando el SDK oficial de Google GenAI (`google-genai`). El script realiza una consulta automatizada al modelo `gemini-3.5-flash` actuando como un experto en Machine Learning.

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente en tu sistema:

* **Python 3.10 o superior**
* Una clave de API de Gemini (**Gemini API Key**). Puedes obtenerla desde [Google AI Studio](https://aistudio.google.com/).

## Estructura del Proyecto

El proyecto debe mantener la siguiente estructura básica de archivos:

```text
gemini-api-connection/
│
├── img/
│   └── evidencia.png     # Captura de pantalla de la terminal
├── .env                  # Archivo opcional con las credenciales de la API
├── .gitignore            # Archivo para evitar subir credenciales a GitHub
├── README.md             # Instrucciones de uso del repositorio
└── main.py               # Código fuente principal en Python