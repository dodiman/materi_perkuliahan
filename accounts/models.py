from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	nama_lengkap = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	nim = models.CharField(max_length=200, null=True)
	alamat = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	# def __str__(self):
		# return self.nama_lengkap