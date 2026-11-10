import logging

import pandas as pd


logger = logging.getLogger(__name__)


def load(df: pd.DataFrame) -> None:

    logger.info(
        f"Preparando carga de {len(df):,} filas"
    )

    # Próximamente:
    # carga hacia BigQuery

    logger.info("Carga finalizada")