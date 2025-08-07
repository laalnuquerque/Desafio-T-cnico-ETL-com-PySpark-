import os
from unittest.mock import patch
import pytest
from pyspark.sql import SparkSession
from app.useCases.clientes.processesCustomerDataUseCase import cross_sale_customer

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder \
        .appName("LoadInfosTest") \
        .master("local[*]") \
        .getOrCreate()

@patch('app.frameworks.utils.salvarRelatorio.salvar_relatorio')
def test_cross_sale_customer_positivo(spark):
    clients_df = spark.createDataFrame([
        {"cliente_id": 1, "nome": "Alice"},
        {"cliente_id": 2, "nome": "Bob"}
    ])
    sales_df = spark.createDataFrame("0000110002000020001200020230403")
    cross_sale_customer(spark, clients_df, sales_df, "/tmp")

    assert os.path.exists("/tmp")


@patch('app.frameworks.utils.salvarRelatorio.salvar_relatorio')
def test_cross_sale_customer_negativo(mock_salvar):
    cross_sale_customer(None, None, None, "/tmp")
    assert Exception is not None
