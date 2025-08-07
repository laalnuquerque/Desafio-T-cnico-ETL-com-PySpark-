import os
from datetime import datetime
from unittest.mock import patch, MagicMock
from app.frameworks.utils.validateDirectory import validate_entry_directory, get_file

@patch("builtins.input", side_effect=["/fake/clientes", "/fake/vendas"])
@patch("os.path.exists", return_value=True)
@patch("os.path.isdir", return_value=True)
@patch("os.listdir")
@patch("os.path.getmtime")
@patch("os.path.isfile", return_value=True)
def test_validate_entry_directory(
    mock_isfile,
    mock_getmtime,
    mock_listdir,
    mock_isdir,
    mock_exists,
    mock_input
):
    mock_listdir.side_effect = [
        ["clientes_2021.csv", "clientes_2022.csv"],
        ["vendas_janeiro.txt", "vendas_fevereiro.txt"]
    ]
    def getmtime_side_effect(path):
        if "2021" in path or "janeiro" in path:
            return datetime(2021, 1, 1).timestamp()
        elif "2022" in path or "fevereiro" in path:
            return datetime(2022, 2, 1).timestamp()
        return 0

    mock_getmtime.side_effect = getmtime_side_effect

    arquivo_clientes, arquivo_vendas = validate_entry_directory()

    assert arquivo_clientes == os.path.join("/fake/clientes", "clientes_2022.csv")
    assert arquivo_vendas == os.path.join("/fake/vendas", "vendas_fevereiro.txt")

def test_get_file_retorna_mais_recente(tmp_path):
    f1 = tmp_path / "clientes_2021.csv"
    f1.write_text("dados")
    os.utime(f1, (1609459200, 1609459200))

    f2 = tmp_path / "clientes_2022.csv"
    f2.write_text("dados")
    os.utime(f2, (1640995200, 1640995200))

    resultado = get_file(str(tmp_path), "clientes", ".csv")
    assert resultado.endswith("clientes_2022.csv")
