from app.frameworks.utils.salvarRelatorio import salvar_relatorio


def cross_sale_customer(spark, clients, sales, path_clients):
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
    try:
        sales.createOrReplaceTempView("vendas_temp_view")
        clients.createOrReplaceTempView("clientes_temp_view")

        resume_clients =  spark.sql("""
        SELECT
            c.cliente_id,
            c.nome,
            CAST(SUM(valor) AS DECIMAL(8,2)) AS total_vendas_produtos,
            COUNT(venda_id) AS quantidade_vendas_produtos,
            CAST(AVG(valor) AS DECIMAL(8,2)) AS ticket_medio
        FROM
            clientes_temp_view c,
            vendas_temp_view s
        WHERE
            c.cliente_id = s.cliente_id
        GROUP BY
            c.cliente_id, c.nome
        ORDER By 
            cliente_id ASC
            """)

        salvar_relatorio(spark,'clientes', resume_clients)
    except Exception as e:
        print(f"Erro ao processar dados de clientes: {e}")


