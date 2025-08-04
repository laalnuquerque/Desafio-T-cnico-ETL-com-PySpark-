def salvar_relatorio(path, dataframe):
    # dataframe.write.mode("overwrite").parquet(path)
    dataframe.write.mode("overwrite").txt(path)

    pass
