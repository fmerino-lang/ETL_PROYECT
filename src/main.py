import logging
from config import INPUT_FILE
from Extract import extract
from Validate import validate_schema, validate_data
from Transform import transform
from Load import load


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

def main() -> None:

    logger.info(
        "========== INICIO ETL =========="
    )

    try:

        datos = extract(INPUT_FILE)

        validate_schema(datos)

        datos = transform(datos)

        validate_data(datos)

        load(datos)

        logger.info(
            "========== ETL EXITOSO =========="
        )

    except Exception:

        logger.exception(
            "========== ETL FALLIDO =========="
        )

        raise


if __name__ == "__main__":
    main()