import csv

# Dados dos clientes
clientes = [
    [10001, "João Silva", "1980-05-12"],
    [10002, "Ana Martins", "1992-11-05"],
    [10014, "Maria Souza", "1995-07-30"],
    [10023, "Carlos Pereira", "2010-03-22"]
    # [5, "Felipe Lima", "2005-09-14"],
    # [6, "Luciana Rocha", "1990-01-27"],
    # [7, "Bruno Fernandes", "2001-12-10"],
    # [8, "Patrícia Oliveira", "1993-06-18"],
    # [9, "Renato Costa", "1987-04-03"],
    # [10, "Amanda Ribeiro", "206-08-21"]
]

# Gerando o arquivo CSV
with open('massa/clientes.csv', mode='w', newline='', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["cliente_id", "nome", "data_nascimento"])  # Cabeçalho
    writer.writerows(clientes)

print("Arquivo 'clientes.csv' gerado com sucesso.")
