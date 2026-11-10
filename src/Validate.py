
import logging

import pandas as pd

logger = logging.getLogger(__name__)

def validate_schema(df: pd.DataFrame) -> None:

    logger.info("Validando estructura del archivo")

    columnas_requeridas = [
        "Nota_credito",
        "Monto",
        "codigo unico",
        "SKU"
    ]

    columnas_faltantes = [

        columna
        for columna in columnas_requeridas
        if columna not in df.columns

    ]

    if columnas_faltantes:
        raise ValueError(
            f"Faltan las columnas: {columnas_faltantes}"
        )

    logger.info("Columnas validadas correctamente")


def validate_data(df: pd.DataFrame) -> None:

    logger.info("Validando calidad de datos")

    if df["Monto"].isna().any():
        raise ValueError(
            "Existen montos nulos"
        )

    logger.info("Montos validados correctamente")
    
