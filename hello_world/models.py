from django.db import models


class Inscricao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona o show ao usuário logado
    tipo_musica = models.CharField(max_length=100)
    horario_disponivel = models.DateTimeField()
    descricao_show = models.TextField()

    def __str__(self):
        return f"{self.usuario.username} - {self.horario_disponivel}"