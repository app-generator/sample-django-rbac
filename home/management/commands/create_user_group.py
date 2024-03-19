from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Creates users, groups, and permissions'

    def handle(self, *args, **options):
        # Create users
        users = ['user_1', 'user_2', 'user_3', 'user_4']
        for username in users:
            User.objects.create_user(username=username, password='password123')

        # Create groups
        group_1 = Group.objects.create(name='group_1')
        group_2 = Group.objects.create(name='group_2')

        # Create permissions
        content_type = ContentType.objects.get_for_model(User)

        # Define permissions for group_1
        permission_1 = Permission.objects.create(
            codename='can_access_route_1',
            name='Can access route 1',
            content_type=content_type,
        )
        group_1.permissions.add(permission_1)

        # Define permissions for group_2
        permission_2 = Permission.objects.create(
            codename='can_access_route_2',
            name='Can access route 2',
            content_type=content_type,
        )
        group_2.permissions.add(permission_2)

        # Add users to groups
        user_1 = User.objects.get(username='user_1')
        user_2 = User.objects.get(username='user_2')
        user_3 = User.objects.get(username='user_3')
        user_4 = User.objects.get(username='user_4')

        group_1.user_set.add(user_1, user_2)
        group_2.user_set.add(user_3, user_4)

        self.stdout.write(self.style.SUCCESS('Users, groups, and permissions created successfully.'))
