import logging
from pathlib import Path

import pandas as pd


logger = logging.getLogger(__name__)


def extract(ruta: Path) -> pd.DataFrame:

    logger.info(f"Leyendo archivo: {ruta.name}")

    if not ruta.exists():
        raise FileNotFoundError(
            f"No existe el archivo: {ruta}"
        )

    df = pd.read_excel(
        ruta,
        dtype=str
    )

    logger.info(
        f"Extraídas {len(df):,} filas"
    )

    return df