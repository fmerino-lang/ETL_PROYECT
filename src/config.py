import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

INPUT_FILE = os.getenv("INPUT_FILE")

if not INPUT_FILE:
    raise ValueError(
        "No se encontró INPUT_FILE en las variables de entorno"
    )

INPUT_FILE = Path(INPUT_FILE)