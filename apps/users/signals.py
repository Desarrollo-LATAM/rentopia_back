from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.owners.models import Owner
from apps.tenants.models import Tenant
from apps.users.models import User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_owner:
            Owner.objects.create(user_id=instance)
        else:
            Tenant.objects.create(user_id=instance)
