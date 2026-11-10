import logging

import pandas as pd


logger = logging.getLogger(__name__)


def transform(
    df: pd.DataFrame
) -> pd.DataFrame:

    logger.info("Iniciando transformación")

    df = df.copy()

    df["Nota_credito"] = (
        df["Nota_credito"]
        .astype("string")
        .str.strip()
    )

    df["codigo unico"] = (
        df["codigo unico"]
        .astype("string")
        .str.strip()
    )

    df["SKU"] = (
        df["SKU"]
        .astype("string")
        .str.strip()
    )

    df["Monto"] = pd.to_numeric(
        df["Monto"],
        errors="coerce"
    )

    logger.info(
        "Transformación finalizada"
    )

    return df