from django.db import models

# Create your models here.
class Teacher(models.Model):
    VACANT_CHOICES = (
        ('OUI','OUI'),
        ('NON','NON'),
    )
    MATTIER_CHOICES = (
        ('Math','Math'),
        ('Physique','Physique'),
        ('EPS','EPS'),
        ('Anglais','Anglais'),
        ('SVT','SVT'),
        ('Philosophie','Philosophie'),
        ('Français','Français'),)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    matiere = models.CharField(choices=MATTIER_CHOICES, max_length=15)
    vacant = models.CharField(max_length=3, choices=VACANT_CHOICES, )
    birth_date = models.DateField(max_length=10)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
    
    def __str__(self):
        return self.first_name