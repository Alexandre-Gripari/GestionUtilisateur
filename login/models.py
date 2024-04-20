from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    CHOICES = (
        ('Scopus', 'Scopus'),
        ('PubMed', 'PubMed'),
        ('Dimensions', 'Dimensions'),
        ('Web of Science', 'Web of Science'),
    )
    choice = models.CharField(max_length=14, choices=CHOICES)

    def __str__(self):
        return self.user.username