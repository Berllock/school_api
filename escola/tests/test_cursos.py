from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso
from escola.serializers import CursoSerializer

class CursosTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)
        self.curso_01 = Curso.objects.create(
            codigo='CT01',descricao='Curso Teste 01',nivel='B'
        )
        self.curso_02 = Curso.objects.create(
            codigo='CT02',descricao='Curso Teste 02',nivel='I'
        )

    def test_requisicao_delete_um_curso(self):
        """Teste de requisição DELETE um curso"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)