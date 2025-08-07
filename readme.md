# Relatório cliente 📜

Bem-vindo ao Sistema de Geração de Relatórios de Clientes e Vendas!
Nosso sistema oferece uma análise para te ajudar no crescimento do seu negócio. Ele calcula automaticamente o ticket médio e gera relatórios detalhados por cliente, facilitando o entendimento do perfil e do valor de cada um.
Sobre as vendas, nós somamos a quantidade total vendida de cada produto e calculamos o ticket médio dos produtos mais vendidos, permitindo que você identifique facilmente os itens com melhor desempenho.
Seja bem-vindo e aproveite ao máximo!

## Arquivo de entrada  🔥<br>
Arquivo cliente:<br>
O arquivo de entrada deve ser no formato CSV e conter informações dos clientes.

Estrutura do arquivo <br>
O arquivo deve apresentar as seguintes colunas, nesta ordem:

| Coluna            | Descrição                      | Formato        |
| ----------------- | ------------------------------ | -------------- |
| `cliente_id`      | Identificador único do cliente | Número inteiro |
| `nome`            | Nome completo do cliente       | Texto          |
| `data_nascimento` | Data de nascimento do cliente  | AAAA-MM-DD     |

<br>
Exemplo de arquivo CSV:

| cliente\_id | nome        | data\_nascimento |
| ----------- | ----------- | ---------------- |
| 1           | João Silva  | 1980-05-12       |
| 2           | Maria Souza | 1995-07-30       |
<br>
Arquivo de Vendas

O arquivo de vendas possui formato posicional com tamanho fixo de 31 caracteres por linha, o formato do arquivo é em TXT. Cada campo possui uma posição específica dentro da linha, conforme o padrão abaixo:

| Campo        | Tamanho (caracteres) | Posições | Descrição                    | Formato                                                    |
| ------------ | -------------------- | -------- | ---------------------------- | ---------------------------------------------------------- |
| `venda_id`   | 5                    | 1 a 5    | Identificador único da venda | Numérico, com zeros à esquerda                             |
| `cliente_id` | 5                    | 6 a 10   | Identificador do cliente     | Numérico, com zeros à esquerda                             |
| `produto_id` | 5                    | 11 a 15  | Identificador do produto     | Numérico, com zeros à esquerda                             |
| `valor`      | 8                    | 16 a 23  | Valor da venda               | Numérico com 2 casas decimais (exemplo: 00012345 = 123,45) |
| `data_venda` | 8                    | 24 a 31  | Data da venda                | Formato YYYYMMDD                                           |

0000110001000011234520230401<br>0000210002000021200020230403

Interpretação das linhas do exemplo

| Campo       | Linha 1       | Linha 2       |
| ----------- | ------------- | ------------- |
| venda\_id   | 00001         | 00002         |
| cliente\_id | 10001         | 10002         |
| produto\_id | 12345         | 12000         |
| valor       | 2023,45 (R\$) | 2023,00 (R\$) |
| data\_venda | 2023-04-01    | 2023-04-03    |

## Arquivo de saída  🔥<br>
O arquivo de saída será gerado no formato CSV e conterá um resumo das vendas por cliente.

Estrutura do arquivo Cliente<br>
O arquivo possui as seguintes colunas:

| Coluna              | Descrição                         | Formato                      |
| ------------------- | --------------------------------- | ---------------------------- |
| `cliente_id`        | Identificador único do cliente    | Número inteiro               |
| `nome`              | Nome completo do cliente          | Texto                        |
| `total_vendas`      | Valor total das vendas do cliente | Número decimal (ex: 2450.00) |
| `quantidade_vendas` | Quantidade total de vendas        | Número inteiro               |
| `ticket_medio`      | Ticket médio das vendas           | Número decimal (ex: 490.00)  |

Descrição<br>
O arquivo representa um resumo consolidado por cliente, contendo:

O total de vendas realizadas pelo cliente.<br>
A quantidade total de vendas efetuadas.<br>
O ticket médio calculado dividindo o total de vendas pela quantidade.

Exemplo de saída (CSV)<br>
```csv
| cliente_id  | nome       | total_vendas  | quantidade _vendas | ticket_medio  |
| ----------- | ---------- | ------------- | ------------------ | ------------- |
| 1           | João Silva | 2450.00       | 5                  | 490.00        |
```
Arquivo de Saída de Vendas por Produto<br>
O arquivo de saída de vendas gera uma balancete resumido das vendas por produto, calculando também o ticket médio.

Estrutura do arquivo<br>
O arquivo conterá as seguintes colunas:

| Coluna                      | Descrição                             | Formato                      |
| --------------------------- | ------------------------------------- | ---------------------------- |
| `produto_id`                | Identificador único do produto        | Número inteiro               |
| `total_vendas_produto`      | Valor total das vendas do produto     | Número decimal (ex: 1450.00) |
| `quantidade_vendas_produto` | Quantidade total de vendas do produto | Número inteiro               |
| `ticket_medio_produto`      | Ticket médio das vendas do produto    | Número decimal (ex: 483.33)  |

Exemplo de saída (CSV)<br>
```csv
| produto_id  | total_vendas_produto   | quantidade_vendas_produto   | ticket_medio_produto   |
| ----------- | ---------------------- | --------------------------- | ---------------------- |
| 10001       | 1450.00                | 3                           | 483.33                 |

```
## 💻 Pré-requisitos

Antes de começar, verifique se você atende aos seguintes requisitos:
* Ter instalado o java v17+
* Ter instalado o python 3.12
* Instalar o pyspark via terminal - pip install pyspark 
* Configurar as variáveis de ambiente User 
        export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-21.jdk/Contents/Home
        export JAVA_HOME="$(/usr/libexec/java_home -v 21.0)"
        export PYSPARK_HADOOP_VERSION=3

## ☕ Usando o sistema dadosCliente

Para usar o sistema, siga estas etapas:
1. Clone o repositório:
   ```bash
   git clone https://github.com/laalnuquerque/Desafio-T-cnico-ETL-com-PySpark-.git
2. Navegue até o diretório do projeto:
   ```bash
   cd dadosCliente
   
3. Execute o script Python para gerar os relatórios opção 1:
   ```bash
    python main.py
    ```
    Ou execute o script Python para gerar os relatórios opção 2:
     Vá até a pasta raiz do projeto, procure o arquivo `main.py` e execute.:<br>
<br>
4. Durante a execução, o sistema solicitará:

- O caminho do arquivo CSV de entrada contendo os dados dos clientes.

- O caminho do arquivo de vendas (formato posicional fixo).

- O caminho de saída para salvar os relatórios gerados.

Os relatórios serão salvos no formato CSV, organizados em pastas separadas:

- cliente/ – Contém os relatórios de resumo por cliente.

- venda/ – Contém os relatórios de resumo por produto.

Essa estrutura facilita a identificação e o acesso aos arquivos gerados.