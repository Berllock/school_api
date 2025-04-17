from django.test import TestCase
from escola.models import  Estudante

class ModelEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@gmail.com',
            cpf = '54831019011',
            data_nascimento = '2023-02-02',
            celular = '86 99999-9999'
        )
    
    def test_verifica_atributos_de_estudante(self):
        """Teste que verifica os atributos do modelo de Estudante"""
        self.assertEqual(self.estudante.nome,'Teste de Modelo')
        self.assertEqual(self.estudante.email,'testedemodelo@gmail.com')
        self.assertEqual(self.estudante.cpf,'54831019011')
        self.assertEqual(self.estudante.data_nascimento,'2023-02-02')
        self.assertEqual(self.estudante.celular,'86 99999-9999')
        
        