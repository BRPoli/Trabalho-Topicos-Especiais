from django.db import models

# Create your models here.
class Tarefas(models.Model):
    id_tarefa = models.AutoField(primary_key=True)
    criador = models.TextField(max_length=50)
    titulo = models.TextField(max_length=55)
    descricao = models.EmailField(max_length=500)
    data_criacao = models.DateTimeField
    status = models.TextField(max_length=100)#pendente,em andamento, concluida