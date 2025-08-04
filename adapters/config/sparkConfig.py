from pyspark.sql import SparkSession

def session_spark():
    spark = SparkSession.builder \
        .master("lc://localhost") \
        .appName("Relatorio Cliente") \
        .config("spark.driver.memory", "4g") \
        .config("spark.executor.memory", "4g") \
        .getOrCreate()

    return spark