import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, DecimalType
from app.entities.vendas.salesEntity import create_dataframe_sales

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder \
        .master("local[*]") \
        .appName("TestSalesDataFrame") \
        .getOrCreate()

def test_create_dataframe_sales_positive(spark):
    df = create_dataframe_sales(spark)

    assert df.count() == 0

    expected_columns = ["venda_id", "cliente_id", "produto_id", "valor", "data_venda"]
    assert df.columns == expected_columns

    schema = df.schema
    assert isinstance(schema["venda_id"].dataType, IntegerType)
    assert isinstance(schema["cliente_id"].dataType, IntegerType)
    assert isinstance(schema["produto_id"].dataType, IntegerType)
    assert isinstance(schema["valor"].dataType, DecimalType)
    assert isinstance(schema["data_venda"].dataType, DecimalType)


def test_create_dataframe_sales_negative():
    with pytest.raises(AttributeError):
        create_dataframe_sales(None)


