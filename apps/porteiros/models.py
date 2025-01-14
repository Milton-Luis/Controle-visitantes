from django.db import models
# from usuarios.models import User


class Porteiro(models.Model):
    user = models.OneToOneField(
        "usuarios.User",
        verbose_name="Usuário",
        on_delete=models.PROTECT,
    )

    nome = models.CharField(verbose_name="Nome completo", max_length=255)
    cpf = models.CharField(verbose_name="cpf", max_length=11)
    telefone = models.CharField(verbose_name="Telefone", max_length=11)
    data_nascimento = models.DateField(
        verbose_name="Data de nascimento", auto_now=False, auto_now_add=False
    )

    class Meta:
        verbose_name="Porteiro"
        verbose_name_plural="Porteiros"
        db_table="porteiro"

    def __str__(self):
        return self.nome