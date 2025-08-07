from pyspark.sql.functions import to_date, col

def load_infos(spark, path, dataframe, sales):
    print(path)
    if sales:
        sales = spark.read.text(path)
        sales.show(truncate=False)
        sales_schema = sales.withColumn("venda_id", col("value").substr(1, 5).cast("int"))
        sales_schema = sales_schema.withColumn("cliente_id", col("value").substr(6, 5).cast("int"))
        sales_schema = sales_schema.withColumn("produto_id", col("value").substr(11, 5).cast("int"))
        sales_schema = sales_schema.withColumn("valor", col("value").substr(16, 8).cast("int"))
        sales_schema = sales_schema.withColumn("data_venda", col("value").substr(24, 8).cast("int"))
        sales_schema = sales_schema.withColumn("data_venda", to_date(col("data_venda"), "yyyyMMdd"))
        sales_schema = sales_schema.drop("value")

        return sales_schema.filter(
            col("venda_id").isNotNull()&
            col("cliente_id").isNotNull() &
            col("produto_id").isNotNull() &
            col("valor").isNotNull()

        )
    else:
         return spark.read.csv(path, schema=dataframe.schema, header=True, inferSchema=False)
