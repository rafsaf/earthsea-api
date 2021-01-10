from django.db.models.signals import post_save
from django.dispatch import receiver

import api.models as models


@receiver(post_save, sender=models.Article)
def create_user_profile(sender, instance, created, **kwargs):
    """ Create initial verified version for new articles """
    if created:
        initial_version = models.Version(
            article=instance,
            text="Ten artykuł nie posiada jeszcze zweryfikowanej zawartości.",
            confirm=True,
        )
        initial_version.save()
