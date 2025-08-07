import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from app.frameworks.database.carregaDados.carregaDados import load_infos

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder \
        .appName("LoadInfosTest") \
        .master("local[*]") \
        .getOrCreate()
tmp_path = '.massa/'

def test_load_infos_positive_sales(spark, tmp_path):
    sales_content = "0000110002000020001200020230403"
    file_path = tmp_path / "test_vendas.txt"
    file_path.write_text(sales_content)

    result_df = load_infos(spark, str(file_path), None, sales=True)
    rows = result_df.collect()

    assert result_df.columns == ["venda_id", "cliente_id", "produto_id", "valor", "data_venda"]
    assert len(rows) == 1
    assert rows[0]["venda_id"] == 1
    assert rows[0]["cliente_id"] == 10002
    assert rows[0]["produto_id"] == 2
    assert rows[0]["valor"] == 12000
    assert str(rows[0]["data_venda"]) == "2023-04-03"

def test_load_infos_positive_dataframe(spark, tmp_path):
    schema = StructType([
        StructField("cliente_id", IntegerType(), True),
        StructField("nome", StringType(), True)
    ])
    df = spark.createDataFrame([], schema)
    csv_path = tmp_path / "temp_clientes.csv"
    csv_path.write_text("cliente_id,nome\n1,Ana\n2,Carlos\n")

    result_df = load_infos(spark, str(csv_path), df, sales=False)
    data = result_df.collect()

    assert result_df.columns == ["cliente_id", "nome"]
    assert len(data) == 2

def test_load_infos_negative_invalid_path(spark):
    with pytest.raises(Exception):
        load_infos(spark, "invalid_path.txt", None, sales=True)
