from pyspark.sql.types import StructType, StructField, IntegerType, DecimalType


def create_dataframe_sales():

    schema = StructType([
        StructField("sales_id", IntegerType(), True),
        StructField("client_id", IntegerType(), True),
        StructField("product_id", IntegerType(), True),
        StructField("value", DecimalType(), True),
        StructField("date_sale", DecimalType(), True)
    ])