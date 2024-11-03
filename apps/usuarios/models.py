from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        user = self.model(
            email=self.normalize_email(email),
        )

        user.is_active = True
        user.is_staff = False
        user.is_superuser = False

        if password:
            user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=True):
        user = self.create_user(email, password=password)

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="Email do usuário", max_length=194, unique=True
    )
    is_active = models.BooleanField(verbose_name="Usuário está ativo", default=True)

    is_staff = models.BooleanField(
        verbose_name="Usuário é da equipe de desenvolvimento", default=False
    )
    is_superuser = models.BooleanField(
        verbose_name="Usuário é um superuser", default=False
    )

    USERNAME_FIELD = "email"
    objects = UserManager()

    class Meta:
        verbose_name = ("Usuário")
        verbose_name_plural = ("Usuários")
        db_table = "user"

    def __str__(self):
        return self.email
