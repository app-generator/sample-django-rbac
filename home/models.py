from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.apps import AppConfig

def create_permissions(sender, **kwargs):
    # Check if the permissions already exist
    route1_permission_exists = Permission.objects.filter(codename='can_access_route1').exists()
    route2_permission_exists = Permission.objects.filter(codename='can_access_route2').exists()

    if not route1_permission_exists:
        # Create model permissions
        route1_permission = Permission.objects.create(
            codename='can_access_route1',
            name='Can Access Route 1',
            content_type=ContentType.objects.get_for_model(Group)
        )

    if not route2_permission_exists:
        route2_permission = Permission.objects.create(
            codename='can_access_route2',
            name='Can Access Route 2',
            content_type=ContentType.objects.get_for_model(Group)
        )

post_migrate.connect(create_permissions, sender=AppConfig)