from django.db.models.signals import post_save
from django.dispatch import receiver
from myapi.models import *
from accounts.models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# jangan lupa diatur di bagain apps.py dan di bagian app (settings.py)
# di ubah di settings.py dengan nama_app.apps.namaconfignya

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='mahasiswa')
		instance.groups.add(group)
		Profil.objects.create(user=instance)

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
	if created == False:
		instance.profil.save()

# @receiver(post_save, sender=Kontrolabsensi)
# def created_absensi(sender, instance, created, **kwargs):
# 	if created:
# 		Absensi.objects.create(kontrolabsensi=instance)

# @receiver(post_save, sender=User)
# def update_absensi(sender, instance, created, **kwargs):
# 	if created == False:
# 		instance.absensi.save()