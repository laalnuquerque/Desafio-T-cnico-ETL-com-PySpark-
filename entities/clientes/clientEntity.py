from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DecimalType

def create_dataframe_clients(spark):
    schema = StructType([
        StructField("client_id", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("date _of _birth", StringType(), True)
    ])

    dataframe_clients = spark.createDataFrame([], schema)
