from django.test import TestCase
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class SerializerEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@gmail.com',
            cpf = '54831019011',
            data_nascimento = '2023-02-02',
            celular = '86 99999-9999'
        )

        self.serializer_estudante = EstudanteSerializer(instance=self.estudante)

    def test_verifica_campos_serializados_de_estudante(self):
        """Teste que verifica os campos que estao sendo serializados de estudante"""
        dados = self.serializer_estudante.data
        self.assertEqual(set(dados.keys()), set(['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']))

    def test_verifica_conteudo_dos_campos_serializados_de_estudante(self):
        """Teste que verifica os conteudo dos campos que estao sendo serializados de estudante"""
        dados = self.serializer_estudante.data
        self.assertEqual(dados['nome'], self.estudante.nome)
        self.assertEqual(dados['email'], self.estudante.email)
        self.assertEqual(dados['cpf'], self.estudante.cpf)
        self.assertEqual(dados['data_nascimento'], self.estudante.data_nascimento)
        self.assertEqual(dados['celular'], self.estudante.celular)