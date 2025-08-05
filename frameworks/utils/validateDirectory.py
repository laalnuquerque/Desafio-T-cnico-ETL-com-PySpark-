import os


def validate_entry_directory(path):
    """
    Valida se o caminho informado é um diretório e se ele existe.

    :param path: O caminho a ser validado.
    :return: Verdadeiro se o caminho for um diretório válido, Falso caso contrário.
    """

    def solicitar_diretorios():
        while True:
            path_clientes = input('Por favor, informe o diretório de clientes: ')
            if os.path.exists(path_clientes):
                print("Diretório de clientes encontrado!")

                while True:
                    path_sales = input('Por favor, informe o diretório de vendas: ')
                    if os.path.exists(path_sales):
                        print("Diretório de vendas encontrado!")
                        return path_clientes, path_sales
                    else:
                        print("Diretório de vendas inválido. Tente novamente.")
            else:
                print("Diretório de clientes inválido. Tente novamente.")

