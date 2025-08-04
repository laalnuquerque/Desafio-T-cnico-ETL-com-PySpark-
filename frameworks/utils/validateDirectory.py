import os


def validate_entry_directory(path):
    """
    Valida se o caminho informado é um diretório e se ele existe.

    :param path: O caminho a ser validado.
    :return: Verdadeiro se o caminho for um diretório válido, Falso caso contrário.
    """
    while True:
        path = input('Por favor informe o diretório de clientes: ')
        if not os.path.exists(path):
            print(f"Diretorio '{path}' nao existe.")
            return False
        if not os.path.isdir(path):
            print(f"Diretorio '{path}' nao existe.")
            return False
        return True

