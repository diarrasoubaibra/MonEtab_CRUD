from django.db import models

# Create your models here.
class User(models.Model):
    pseudo_name = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.pseudo_name