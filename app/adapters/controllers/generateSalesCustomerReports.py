from app.entities.vendas.salesEntity import create_dataframe_sales
from app.entities.clientes.clientEntity import create_dataframe_clients
from app.adapters.config.sparkConfig import session_spark
from app.frameworks.database.carregaDados import carregaDados
from app.frameworks.utils.validateDirectory import validate_entry_directory
from app.useCases.clientes.processesCustomerDataUseCase import cross_sale_customer
from app.useCases.vendas.processesSalesInformationUseCase import balance_by_product

def generate_sales_customer_reports():
    """ Gera relatórios de vendas e clientes a partir de dados carregados em DataFrames."""
    try:
        spark = session_spark()
        clientes = create_dataframe_clients(spark)
        vendas = create_dataframe_sales(spark)

        path_clientes, path_vendas = validate_entry_directory()

        cliente = carregaDados.load_infos(spark, path_clientes, clientes, False)
        venda = carregaDados.load_infos(spark, path_vendas, vendas, True)

        cross_sale_customer(spark, cliente, venda, path_clientes)
        balance_by_product(spark, venda)
    except Exception as e:
        print(f"Erro ao gerar relatórios: {e}")