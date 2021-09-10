from django.db.models.signals import post_save
from django.dispatch import receiver
from myapi.models import *

# jangan lupa diatur di bagain apps.py dan di bagian app (settings.py)
# di ubah di settings.py dengan nama_app.apps.namaconfignya

@receiver(post_save, sender=Anggota)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(anggota=instance)

@receiver(post_save, sender=Anggota)
def update_profile(sender, instance, created, **kwargs):
	if created == False:
		instance.profile.save()