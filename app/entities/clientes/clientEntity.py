from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DecimalType

def create_dataframe_clients(spark):
    schema = StructType([
        StructField("cliente_id", IntegerType(), True),
        StructField("nome", StringType(), True),
        StructField("data_nascimento", StringType(), True)
    ])

    return spark.createDataFrame([], schema)
