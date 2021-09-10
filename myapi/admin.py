from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import *

@admin.register(Mapel)
class MapelAdmin(ImportExportModelAdmin):
	pass

@admin.register(Arsip)
class ArsipAdmin(ImportExportModelAdmin):
	pass

@admin.register(Matakul)
class MatakulAdmin(ImportExportModelAdmin):
	pass	

@admin.register(Kontrolabsensi)
class KontrolabsensiAdmin(ImportExportModelAdmin):
	pass

@admin.register(Absensi)
class AbsensiAdmin(ImportExportModelAdmin):
	pass