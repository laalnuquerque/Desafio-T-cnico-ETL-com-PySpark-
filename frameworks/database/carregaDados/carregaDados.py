def load_infos(spark, path, sales):
    return spark.DataFrameReader.txt(path, schema=sales.schema, header=True, inferSchema=False)