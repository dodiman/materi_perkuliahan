from import_export import resources, fields, widgets
from .models import *

class MapelResource(resources.ModelResource):
	class Meta:
		model = Mapel

# class DatasResource(resources.ModelResource):
# 	class Meta:
# 		model = Datas

class CustomResource(resources.Resource):
	nama_pelajaran = fields.Field(column_name='nama_pelajaran', attribute="nama_pelajaran")
	kode_pelajaran = fields.Field(column_name='kode_pelajaran', attribute="kode_pelajaran")

	# class Meta:
		# model = Mapel
