from app.adapters.config.sparkConfig import session_spark

def test_session_spark_creation():
    spark = session_spark()

    assert spark is not None
    assert spark.sparkContext.appName == "Relatorio Cliente"
    assert spark.conf.get("spark.driver.memory") == "4g"
    assert spark.conf.get("spark.executor.memory") == "4g"

    spark.stop()



