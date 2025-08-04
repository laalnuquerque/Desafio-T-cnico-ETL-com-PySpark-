from frameworks.utils.salvarRelatorio import salvar_relatorio


def cross_sale_customer(spark, sales, clients):
    """
    Processa os dados de clientes e vendas para gerar um resumo de vendas por cliente.

    Passos:
    1. Realizar um join entre as tabelas de vendas e clientes usando o campo cliente_id.
    2. Calcular para cada cliente:
       - Valor total de vendas.
       - Quantidade total de vendas realizadas.
       - Ticket médio (valor médio por venda).
    3. Gerar um arquivo estruturado (resumo_clientes) contendo:
       - cliente_id
       - nome
       - total_vendas
       - quantidade_vendas
       - ticket_medio
    """
    sales.CreateOrTempView("sales_temp_view")
    clients.CreateOrReplaceTempView("clients_temp_view")

    resume_clients =  spark.sql("""
    SELECT
        c.cliente_id,
        c.nome,
        SUM(s.value) AS valor_total_vendas,
        COUNT(s.sales_id) AS quantidade_total_vendas,
        valor_total_venda/quantidade_total_vendas AS ticket_medio
    FROM
        clients_temp_view c,
        sales_temp_view s
    WHERE
        c.cliente_id = s.cliente_id
    ORDER By asc.cliente_id
        """)

    salvar_relatorio(spark, resume_clients)

