from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer


class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_01 = Estudante.objects.create(
            nome = 'Teste estudante UM',
            email = 'testeestudante01@gmail.com',
            cpf ='68224431002',
            data_nascimento='2024-01-02',
            celular = '86 99999-9999'
        )
        self.estudante_02 = Estudante.objects.create(
            nome = 'Teste estudante DOIS',
            email = 'testeestudante02@gmail.com',
            cpf ='70261486055',
            data_nascimento='2024-01-02',
            celular = '86 99999-9999'
        )

    def test_requisicao_get_para_listar_estudantes(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_requisicao_get_para_listar_um_estudante(self):
        """Teste de requisição GET para um estudante"""
        response = self.client.get(self.url + '1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance=dados_estudante).data
        self.assertEqual(response.data, dados_estudante_serializados)

    def test_requisicao_post_para_criar_um_estudante(self):
        """Teste de requisição POST para um estudante"""
        dados = {
            'nome': 'teste',
            'email': 'teste@gmail.com',
            'cpf': '78232809060',
            'data_nascimento': '2002-03-23',
            'celular': '11 99999-9999'
        }
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_um_estudante(self):
        """Teste de requisição DELETE um estudante"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        dados = {
            'nome': 'teste',
            'email': 'testeput@gmail.com',
            'cpf': '69864971050',
            'data_nascimento': '2003-05-09',
            'celular': '11 77777-7777'
        }
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)