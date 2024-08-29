from django.db import models

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = (
        ('h','Homme'),
        ('f','Femme'),
    )
    CLASSE_CHOICES = (
        ('terminale','terminale'),
        ('premiere','première'),
        ('seconde','seconde'),
        ('troisieme','troisième'),
        ('quatrieme','quatrième'),
        ('cinquieme','cinquième'),
        ('sixieme','sixième'),
    )
    firs_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=255)
    Genre = models.CharField(max_length=30, choices=GENDER_CHOICES)
    Matricule= models.CharField(max_length=15)
    birth_date = models.DateField(max_length=10)
    Classe= models.CharField(max_length=15, choices=CLASSE_CHOICES)
    phone_number=models.CharField(max_length=30)
    city=models.CharField(max_length=30)

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
    def __str__(self):
        return f"{self.firs_name} {self.last_name}"