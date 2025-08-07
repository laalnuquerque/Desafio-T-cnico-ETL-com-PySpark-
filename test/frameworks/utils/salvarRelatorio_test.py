import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
from app.frameworks.utils.validateDirectory import validate_entry_directory, get_file

class TestFileValidation(unittest.TestCase):

    @patch('builtins.input')
    @patch('os.path.exists')
    @patch('os.path.isdir')
    @patch('os.listdir')
    @patch('os.path.getmtime')
    @patch('os.path.isfile')
    def test_validate_entry_directory_completo(
            self, mock_isfile, mock_getmtime, mock_listdir, mock_isdir, mock_exists, mock_input
    ):
        mock_input.side_effect = ['/clientes', '/vendas']
        mock_exists.return_value = True
        mock_isdir.return_value = True
        mock_isfile.return_value = True

        def fake_listdir(path):
            if path == '/clientes':
                return ['clientes_20230801.csv']
            elif path == '/vendas':
                return ['vendas_20230801.txt']
            return []

        mock_listdir.side_effect = fake_listdir
        mock_getmtime.return_value = datetime.now().timestamp()

        clientes, vendas = validate_entry_directory()
        self.assertTrue(clientes.endswith('clientes_20230801.csv'))
        self.assertTrue(vendas.endswith('vendas_20230801.txt'))

    @patch('os.path.getmtime')
    @patch('os.listdir')
    @patch('os.path.isfile')
    def test_get_file_positivo(self, mock_isfile, mock_listdir, mock_getmtime):
        mock_listdir.return_value = ['clientes_20230801.csv', 'clientes_20230802.csv']
        mock_isfile.return_value = True

        mock_getmtime.side_effect = [
            (datetime.now() - timedelta(days=1)).timestamp(),
            datetime.now().timestamp()
        ]

        path = '/fake_dir'
        result = get_file(path, 'clientes', '.csv')
        self.assertTrue(result.endswith('clientes_20230802.csv'))

    @patch('os.path.getmtime')
    @patch('os.listdir')
    @patch('os.path.isfile')
    def test_get_file_negativo(self, mock_isfile, mock_listdir, mock_getmtime):
        mock_listdir.return_value = ['not_match.txt', 'image.png']
        mock_isfile.return_value = True
        mock_getmtime.return_value = datetime.now().timestamp()

        path = '/fake_dir'
        result = get_file(path, 'clientes', '.csv')
        self.assertIsNone(result)

