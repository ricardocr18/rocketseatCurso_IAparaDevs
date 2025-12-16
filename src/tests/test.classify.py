import unittest
from src.classify import classify_message

class TestClassifyMessage(unittest.TestCase):

    def test_classify_venda(self):
        message = "Estou interessado em comprar um produto."
        result = classify_message(message)
        self.assertEqual(result, "venda")

    def test_classify_suporte(self):
        message = "Preciso de ajuda com meu pedido."
        result = classify_message(message)
        self.assertEqual(result, "suporte")

    def test_classify_unknown(self):
        message = "Qual é o horário de funcionamento da loja?"
        result = classify_message(message)
        self.assertNotIn(result, ["venda", "suporte"])

if __name__ == '__main__':
    unittest.main()