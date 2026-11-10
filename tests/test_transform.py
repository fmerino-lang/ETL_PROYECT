import pandas as pd

from src.Transform import transform


def test_transform_convierte_monto():

    df = pd.DataFrame({
        "Nota_credito": ["NC001"],
        "Monto": ["15000"],
        "codigo unico": ["ABC123"],
        "SKU": ["SKU001"]
    })

    resultado = transform(df)

    assert resultado["Monto"].iloc[0] == 15000