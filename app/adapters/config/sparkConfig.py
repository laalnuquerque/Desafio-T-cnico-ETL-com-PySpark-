from pyspark.sql import SparkSession

def session_spark():
    try:
        spark = SparkSession.builder \
            .master("local[*]") \
            .appName("Relatorio Cliente") \
            .config("spark.driver.memory", "4g") \
            .config("spark.executor.memory", "4g") \
            .getOrCreate()

        return spark
    except Exception as e:
        raise f"Erro ao criar sessão Spark: {e}"
