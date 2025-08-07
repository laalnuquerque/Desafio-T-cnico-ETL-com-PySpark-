import os
from datetime import datetime

arquivo_mais_recente = None
data_mais_recente = None

def validate_entry_directory():
    """
    Valida se o caminho informado é um diretório e se ele existe.

    :param path: O caminho a ser validado.
    :return: Verdadeiro se o caminho for um diretório válido, Falso caso contrário.
    """
    while True:
        path_clientes = input('Por favor, informe o diretório de clientes: ')
        if os.path.exists(path_clientes) and os.path.isdir(path_clientes):
            arquivo_clientes = get_file(path_clientes, 'clientes', '.csv')
            print("Diretório de vendas encontrado!")
            break
        else:
            print("Diretório de clientes inválido. Tente novamente.")

    while True:

        path_venda = input('Por favor, informe o diretório de vendas: ')
        if os.path.exists(path_venda) and os.path.isdir(path_venda):
            arquivo_vendas = get_file(path_venda, 'vendas','.txt')
            print("Diretório de vendas encontrado!")
            print(arquivo_vendas)
            return arquivo_clientes, arquivo_vendas
        else:
            print("Diretório de vendas inválido. Tente novamente.")

def get_file(diretorio, nome_relatorio, formarto):
    data_mais_recente = None
    arquivo_mais_recente = None
    nomes_arquivos = [f for f in os.listdir(diretorio) if f.endswith(formarto)]
    for nome_arquivo in sorted(nomes_arquivos):
        caminho_completo = os.path.join(diretorio, nome_arquivo)
        if os.path.isfile(caminho_completo) and nome_relatorio in nome_arquivo:
            data_modificacao = datetime.fromtimestamp(os.path.getmtime(caminho_completo))

            if data_mais_recente is None or data_modificacao > data_mais_recente:
                data_mais_recente = data_modificacao
                arquivo_mais_recente = caminho_completo

    return arquivo_mais_recente