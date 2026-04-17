from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create test users for the application'

    def handle(self, *args, **kwargs):
        test_users = [
            ('john', 'john@test.com', 'test123'),
            ('jane', 'jane@test.com', 'test123'),
            ('bob', 'bob@test.com', 'test123'),
        ]
        
        for username, email, password in test_users:
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                self.stdout.write(f'Created user: {username} (password: {password})')
            else:
                self.stdout.write(f'User {username} already exists')
        
        self.stdout.write(self.style.SUCCESS('Test users created successfully!'))
