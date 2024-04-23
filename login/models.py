from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver



class DataBase(models.Model):
    CHOICES = (
        ('Scopus', 'Scopus'),
        ('PubMed', 'PubMed'),
        ('Dimensions', 'Dimensions'),
        ('Web of Science', 'Web of Science'),
    )
    name = models.CharField(max_length=14, choices=CHOICES, unique=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    databases = models.ManyToManyField(DataBase)

    def __str__(self):
        return self.user.username
    
@receiver(post_migrate)
def create_databases(sender, **kwargs):
    for choice, _ in DataBase.CHOICES:
        DataBase.objects.get_or_create(name=choice)
