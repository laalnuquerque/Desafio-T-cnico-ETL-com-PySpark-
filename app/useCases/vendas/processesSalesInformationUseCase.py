from app.frameworks.utils.salvarRelatorio import salvar_relatorio


def balance_by_product(spark, sales):
    """
    Função para gerar um resumo de vendas por produto.
    Retorna um DataFrame com as seguintes colunas:
    - produto_id
    - total_vendas_produto
    - quantidade_vendas_produto
    - ticket_medio_produto
    """
    try:
        sales.createOrReplaceTempView("vendas_temp_view")

        resume_sales =  spark.sql(""" 
        SELECT
             produto_id as produto_id,
             CAST(SUM(valor) AS DECIMAL(8,2)) AS total_vendas_produtos,
             COUNT(venda_id) AS quantidade_vendas_produtos,
             CAST(AVG(valor) AS DECIMAL(8,2)) AS ticket_medio
             
        FROM
            vendas_temp_view
        GROUP BY
            produto_id
        """)
        salvar_relatorio(spark,'vendas', resume_sales)
    except Exception as e:
        print(f"Erro ao processar dados de vendas: {e}")

