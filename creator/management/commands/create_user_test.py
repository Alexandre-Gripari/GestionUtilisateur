from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from login.models import UserProfile

class Command(BaseCommand):
    help = 'Create a test user'

    def handle(self, *args, **options):

        user = User.objects.create_user(
            username='testuser2', 
            email='testuser@example.com', 
            password='testpassword2',
            first_name='Test',
            last_name='User'
        )

    
        UserProfile.objects.create(user=user, choice='Scopus')

        self.stdout.write(self.style.SUCCESS('Test user created.'))