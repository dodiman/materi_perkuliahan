from django.db import models
from django.contrib.auth.models import User

class Mapel(models.Model):
	kode_pelajaran = models.CharField(max_length=200, null=True, blank=True)
	nama_pelajaran = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	# def __str__(self):
		# return self.kode_pelajaran

class Arsip(models.Model):
	keterangan = models.CharField(max_length=200, null=True, blank=True)
	file_pelajaran = models.FileField(upload_to='materi/')
	mapel = models.ForeignKey(Mapel, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

class Matakul(models.Model):
	kode_matkul = models.CharField(max_length=200, null=True, blank=True)
	nama_matkul = models.CharField(max_length=200, null=True, blank=True)
	mapel = models.ManyToManyField(Mapel)

class Kontrolabsensi(models.Model):
	keterangan = models.CharField(max_length=200, null=True, blank=True)
	status = models.BooleanField()
	mapel = models.ForeignKey(Mapel, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_updated = models.DateTimeField(auto_now=True, null=True)

class Absensi(models.Model):
	nama  = models.CharField(max_length=200, null=True, blank=True)
	nim = models.CharField(max_length=200, null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	kontrolabsensi = models.ForeignKey(Kontrolabsensi, on_delete=models.CASCADE, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_updated = models.DateTimeField(auto_now=True, null=True)

# class Tugas(models.Model):
# 	nama = models.CharField(max_length=200, null=True, blank=True)
# 	nim = models.CharField(max_length=200, null=True, blank=True)
# 	keterangan = models.CharField(max_length=200, null=True, blank=True)
# 	file_tugas = models.FileField(upload_to='tugas/')
# 	matakul = models.ForeignKey(Matakul, on_delete=models.CASCADE)
	# date_created = models.DateTimeField(auto_now_add=True, null=True)
	# date_updated = models.DateTimeField(auto_now=True, null=True)

