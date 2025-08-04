from frameworks.utils.salvarRelatorio import salvar_relatorio


def balance_by_product(spark, sales):
    """
    Função para gerar um resumo de vendas por produto.
    Retorna um DataFrame com as seguintes colunas:
    - produto_id
    - total_vendas_produto
    - quantidade_vendas_produto
    - ticket_medio_produto
    """
    sales.createOrRepleceTempView("sales_temp_view")

    reasume_sales =  spark.sql(""" 
    SELECT
         product_id as produto_id,
         SUM(value) AS total_vendas_produto,
         COUNT(sales_id) AS quantidade_venedas_produto,
         total_vendas_produtos/quantidade_vendas_produto as ticket_medio_produto
    FROM
        sales_temp_view
    GROUP BY
        product_id
    """)

    salvar_relatorio(spark, reasume_sales)

