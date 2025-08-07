import os
import shutil


def salvar_relatorio(spark, path, dataframe):
    try:
        path_raiz = input("Informe o caminho para salvar o relatório: ")
        path_final = os.path.join(path_raiz,"relatorio", path)
        if os.path.exists(path_final):
            shutil.rmtree(path_final)
        dataframe.coalesce(1).write.option("header", True).mode("overwrite").csv(f"{path_final}")
        clientes = spark.read.csv(path_final, schema=dataframe.schema, header=True, inferSchema=False)
        if path == "clientes":
            for linha in clientes.collect():
                name = linha.nome
                path_nome_cliente = os.path.join(f"{path_final}/{name}")
                spark.createDataFrame([linha], schema=dataframe.schema).coalesce(1).write.mode("overwrite").option("header", True).csv(path_nome_cliente)
                try:
                    for file in os.listdir(path_nome_cliente):
                        if file.startswith("part-"):
                            arquivo_antigo = os.path.join(path_nome_cliente, file)
                            arquivo_novo = os.path.join(path_nome_cliente, f"{name}.csv")
                            os.rename(arquivo_antigo, arquivo_novo)
                            print(f"Arquivo renomeado com sucesso: {path_nome_cliente}")
                except FileNotFoundError:
                    print(f"Erro: Arquivo não encontrado em {path_nome_cliente}")
                except Exception as e:
                    print(f"Erro ao renomear o arquivo em {path_nome_cliente}: {e}")
        print(f"Relatório salvo com sucesso em: {path_final}")
    except Exception as e:
        print(f"Erro ao salvar o relatório: {e}")
    pass
