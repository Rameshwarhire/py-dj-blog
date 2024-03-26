from django.db.models.signals import post_save 
from django.contrib.auth.models import User # This import for add data in auth_user table
from django.dispatch import receiver
from .models import Profile # This import for add data in user_profile table

# This section make changes in user table
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# This section make changes in profile table
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()