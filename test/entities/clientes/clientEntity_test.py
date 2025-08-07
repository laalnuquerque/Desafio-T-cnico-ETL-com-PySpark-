import pytest
from pyspark.sql import SparkSession
from app.entities.clientes.clientEntity import create_dataframe_clients


@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder \
        .master("local") \
        .appName("Test") \
        .getOrCreate()


def test_create_dataframe_clients_positive(spark):
    df = create_dataframe_clients(spark)

    assert df.count() == 0

    expected_fields = ["cliente_id", "nome", "data_nascimento"]
    assert df.columns == expected_fields

    field_types = [field.dataType for field in df.schema.fields]
    assert str(field_types[0]) == "IntegerType()"
    assert str(field_types[1]) == "StringType()"
    assert str(field_types[2]) == "StringType()"


import pytest

def test_create_dataframe_clients_negative():
    with pytest.raises(AttributeError):
        create_dataframe_clients(None)
