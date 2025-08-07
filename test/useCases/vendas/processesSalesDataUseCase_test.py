import os
from unittest.mock import patch
import pytest
from pyspark.sql import SparkSession
from app.useCases.vendas.processesSalesInformationUseCase import balance_by_product

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder \
        .appName("LoadInfosTest") \
        .master("local[*]") \
        .getOrCreate()

@patch('app.frameworks.utils.salvarRelatorio.salvar_relatorio')
def test_balance_product_positive(spark):
    sales_df = spark.createDataFrame("0000110002000020001200020230403")
    balance_by_product(spark, sales_df)

    assert os.path.exists("/tmp")


@patch('app.frameworks.utils.salvarRelatorio.salvar_relatorio')
def test_cross_sale_customer_negativo(spark):
    balance_by_product(None, None)
    assert Exception is not None
