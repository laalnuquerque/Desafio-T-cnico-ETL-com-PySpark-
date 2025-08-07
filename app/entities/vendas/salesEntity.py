from pyspark.sql.types import StructType, StructField, IntegerType, DecimalType


def create_dataframe_sales(spark):

    schema = StructType([
        StructField("venda_id", IntegerType(), True),
        StructField("cliente_id", IntegerType(), True),
        StructField("produto_id", IntegerType(), True),
        StructField("valor", DecimalType(), True),
        StructField("data_venda", DecimalType(), True)
    ])

    return spark.createDataFrame([], schema=schema)