from django.urls import path

from . import views

urlpatterns = [
	# path('remove_data', views.remove_data, name="remove_data_myapi"),   # post
	# path('create_data', views.create_data, name="create_data_myapi"),    # post
	# path('detail_data/<int:id>', views.detail_data, name="detail_data_myapi"),  
	# path('update_data_anggota/<int:id>', views.update_data_anggota, name="update_data_anggota_myapi"),  # post
	# path('update_data_profile/<int:id>', views.update_data_profile, name="update_data_profile_myapi"),  # post
	# path('cari_data', views.cari_data, name="cari_data_myapi"),   # post

	path('simulasi', views.simulasi, name="simulasi_myapi"),  
	path('update_arsip/<int:id>', views.update_arsip, name="update_arsip_myapi"),             # post
	path('update_profil', views.update_profil, name="update_profil_myapi"),             # post
	path('update_mapel/<int:id>', views.update_mapel, name="update_mapel_myapi"),             # post
	path('detail_mapel/<int:id>', views.detail_mapel, name="detail_mapel_myapi"),  
	path('remove_data_mapel', views.remove_data_mapel, name="remove_data_mapel_myapi"),   # post
	path('remove_data_arsip', views.remove_data_arsip, name="remove_data_arsip_myapi"),   # post
	path('data_mapel', views.data_mapel, name="data_mapel_myapi"),    # post
	path('create_arsip', views.create_arsip, name="create_arsip_myapi"),    # post
	path('create_mapel', views.create_mapel, name="create_mapel_myapi"),    # post
	path('arsip/<int:id>', views.arsip, name="arsip_myapi"),  
	
	# absensi
	path('lihat_absensi', views.lihat_absensi, name="lihat_absensi_myapi"),  			#  post
	path('kontrol_absensi', views.kontrol_absensi, name="kontrol_absensi_myapi"),  			# get / post
	path('absensi', views.absensi, name="absensi_myapi"),  			# get / post

	# untuk download file dalam bentuk excel
	path('export_file', views.export_file, name="export_file_myapi"),  
	
	path('akun', views.akun, name="akun_myapi"),  
	path('autentifikasi', views.autentifikasi, name="autentifikasi_myapi"),  
	path('halamanlogin', views.halamanlogin, name="halamanlogin_myapi"),  
	path('logoutuser', views.logoutuser, name="logoutuser_myapi"),  
	path('mapel', views.mapel, name="mapel_myapi"),  
	path('', views.mydata, name="mydata_myapi"),  
]