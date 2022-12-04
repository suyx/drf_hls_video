from django.contrib.auth.models import AbstractUser
from django.db import models
from shared.models import UUIDModel


class User(AbstractUser, UUIDModel):
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.username}, id: {self.id}"
