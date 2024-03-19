# management/commands/setup_access_control.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from django_prbac.models import Role, Grant, UserRole

class Command(BaseCommand):
    help = 'Sets up access control'

    def handle(self, *args, **options):
        # Create users
        users = ['user_1', 'user_2', 'user_3', 'user_4']
        for username in users:
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password('password123')
                user.save()
                self.stdout.write(self.style.SUCCESS(f'User {username} created'))

        # Create groups
        for user in User.objects.filter(username__in=users):
            Role.objects.create(
                name=user.username,
                slug=user.username,
                description='Role for django user: %s' % user.username
            )

        route_1 = Role.objects.create(name='route_1', slug='route_1', description='May view route 1')
        route_2 = Role.objects.create(name='route_2', slug='route_2', description='May route 2')

        user_1 = Role.objects.get(name='user_1')
        user_2 = Role.objects.get(name='user_2')
        user_3 = Role.objects.get(name='user_3')
        user_4 = Role.objects.get(name='user_4')


        Grant.objects.create(from_role=user_1, to_role=route_1)
        Grant.objects.create(from_role=user_2, to_role=route_1)
        Grant.objects.create(from_role=user_3, to_role=route_2)
        Grant.objects.create(from_role=user_4, to_role=route_2)

        self.stdout.write(self.style.SUCCESS('Access control setup completed successfully.'))
