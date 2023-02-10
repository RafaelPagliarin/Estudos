"""
Unittest - Antes e Apos hooks

hooks são os testes. Ou seja, a execução dos testes.

setup() -> executado antes de cada método de test, é util para criarmos instancias de objetos e outros dados

tearDown() -> executado ao final de cada metodo de teste. É util para excluir dados e fechar conexões com bancos de dados

"""

import unittest


class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configurações do setUp()
        pass

    def test_primeiro(self):
        #setUp vai rodar antes do teste
        #tearDown() vai rodar após o teste
        pass

    def test_segundo(self):
        #setUp vai rodar antes do teste
        #tearDown() vai rodar após o teste
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass

    

