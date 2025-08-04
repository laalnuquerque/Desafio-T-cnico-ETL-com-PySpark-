import os

from entities.vendas.salesEntity import create_dataframe_sales
from entities.clientes.clientEntity import create_dataframe_clients
from adapters.config.sparkConfig import session_spark
from frameworks.database.carregaDados import carregaDados
from frameworks.utils.validateDirectory import validate_entry_directory

if __name__ == "__main__":
    spark = session_spark()
    clients = create_dataframe_clients(spark)
    sales = create_dataframe_sales()

    path_clientes = validate_entry_directory()
    )

    while True:
        path_clientes = input('Por favor informe o diretório de clientes: ')
        if os.path.exists(path_clientes):
            print("Diretório encontrado!")
            break
        else:
            print("Diretório inválido. Tente novamente.")

    while False:
        path_clientes = input('Por favor informe o diretorio de clientes: ')


    if True:
        pass
    else

    path_vendas = input('Por favor informe o diretorio de vendas: ')

    carregaDados.load_infos(spark, clients)
    carregaDados.load_infos(spark, sales)




