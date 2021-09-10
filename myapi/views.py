from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from myapi.serializers import *
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from django.http import JsonResponse
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from accounts.decorators import unauthenticated_user, allowed_users, admin_only

from django.core.exceptions import ObjectDoesNotExist
import warnings
warnings.filterwarnings('ignore')

from django.db.models import Q

# import pandas as pd
# import numpy as np

# apriori
# from mlxtend.preprocessing import TransactionEncoder
# from mlxtend.frequent_patterns import apriori, fpmax, fpgrowth
# from mlxtend.frequent_patterns import association_rules

from django.contrib import messages

# modul yang say buat
from .modulku import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.models import User
from accounts.models import *

from .models import *
from accounts.models import *

# untuk import export
from .resources import *
from tablib import Dataset

# export data ke excel
def export_file(request):
	# mydata_resource = MapelResource()
	# custom_resource = CustomResource()
	# myqueryset = Mapel.objects.all()
	# mydict = [
	# 	{"nama_pelajaran": "mantap", "kode_pelajaran": "okedong"}
	# ]
	# df = pd.DataFrame(myqueryset.values())
	# df = df[['nama_pelajaran', 'kode_pelajaran']]
	# dataset = custom_resource.export(mydict)  # file bisa diletakkan disini
	# print(df)
	# print("pembatas")
	# print(dataset.json)

	# response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
	# response['Content-Disposition'] = 'attachment; filename="mydata.xlsx"'
	# return response
	return HttpResponse('okelah mantap')

@login_required(login_url='halamanlogin_myapi')
@allowed_users(allowed_roles=['admin','mahasiswa'])
@csrf_exempt
def update_profil(request):
	if request.method == 'GET':
		return HttpResponse('harusnya method post')

	if request.method == 'POST':
		context = {
			"id": None,
			"akun": None,
			"profil": None,
		}

		if request.user.is_authenticated:
			idnya = request.user.id
			akun = User.objects.get(pk=idnya)
			profil = akun.profil

			# ak = User.objects.get(pk=7)
			# sem = ak.profil
			# proses update profil

			form = ProfilForm(request.POST or None, instance=profil)
			print(form.errors)
			print(form.is_valid())
			if form.is_valid():
				form.save()
				print('sukses disimpan')

			akun_serializer = akun.username
			profil_serializer = ProfilSerializer(profil)

			context = {
				"id": idnya,
				"akun": akun_serializer,
				"profil": profil_serializer.data,
			}
		return JsonResponse(context)

def autentifikasi(request):
	context = {
		"id": None,
		"akun": None,
		"profil": None,
	}

	if request.user.is_authenticated:
		idnya = request.user.id
		akun = User.objects.get(pk=idnya)
		profil = akun.profil

		akun_serializer = akun.username
		profil_serializer = ProfilSerializer(profil)

		context = {
			"id": idnya,
			"akun": akun_serializer,
			"profil": profil_serializer.data,
		}
	return JsonResponse(context)


def logoutuser(request):
	logout(request)
	return redirect('login_index')

@unauthenticated_user
def halamanlogin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('halamanlogin_myapi')
		else:
			messages.info(request, 'Username OR password is incorrect')
	return render(request, 'login.html')

@login_required(login_url='halamanlogin_myapi')
@allowed_users(allowed_roles=['admin','mahasiswa'])
@csrf_exempt
def mydata(request):
	if request.method == 'GET':
		# anggota = Anggota.objects.all()
		# serializer= AnggotaSerializer(anggota, many=True)

		# # untuk paginasi
		# page = request.GET.get('page', 1)
		# limit = 10
		# alamat = request.build_absolute_uri()

		# return JsonResponse(paginasinya(serializer.data, page, limit, safe=False, alamat=alamat))
		# return HttpResponse('mantap');
		return redirect('index')

@login_required(login_url='halamanlogin_myapi')
@allowed_users(allowed_roles=['admin','mahasiswa'])
@csrf_exempt
def mapel(request):
	db = Mapel.objects.all()
	mapel_serializer = MapelSerializer(db, many=True)

	# untuk paginasi
	page = request.GET.get('page', 1)
	limit = 10
	alamat = request.build_absolute_uri()


	context = paginasinya(mapel_serializer.data, page, limit, safe=False, alamat=alamat)
	return JsonResponse(context)
	# return HttpResponse('oke dong');

@login_required(login_url='halamanlogin_myapi')
@allowed_users(allowed_roles=['admin','mahasiswa'])
@csrf_exempt
def arsip(request, id):
	initialAwal = {
	    "count": "",
	    "current": "",
	    "previous_page": None,
	    "next_page": False,
	    "previous": "0",
	    "next": False,
	    "total_data": "",
	    "data": [],
	    "safe": False,
	    "alamat": request.build_absolute_uri()
	}

	matapelajaran = Mapel.objects.get(pk=id)

	try:
		data_arsip = matapelajaran.arsip_set.all()
		serializer = ArsipSerializer(data_arsip, many=True)

		# untuk paginasi
		page = request.GET.get('page', 1)
		limit = 10
		alamat = request.build_absolute_uri()
		
		context = paginasinya(serializer.data, page, limit, safe=False, alamat=alamat)
	except (ObjectDoesNotExist, AttributeError, TypeError):
		context = initialAwal

	return JsonResponse(context)

@login_required(login_url='halamanlogin_myapi')
@allowed_users(allowed_roles=['admin','mahasiswa'])
@csrf_exempt
def create_arsip(request):    
	if request.method == 'POST':
		anggota_form = ArsipForm(request.POST or None)
		if anggota_form.is_valid():
			anggota_form.save()

	return redirect('data_mapel_myapi')

@login_required(login_url='halamanlogin_myapi')
@allowed_users(allowed_roles=['admin','mahasiswa'])
@csrf_exempt
def create_mapel(request):    
	if request.method == 'POST':
		anggota_form = MapelForm(request.POST or None)
		if anggota_form.is_valid():
			anggota_form.save()

	return redirect('data_mapel_myapi')

@login_required(login_url='halamanlogin_myapi')
@allowed_users(allowed_roles=['admin','mahasiswa'])
@csrf_exempt
def data_mapel(request):    
	mapel = Mapel.objects.all()
	serializer= MapelSerializer(mapel, many=True)

	# untuk paginasi
	page = request.GET.get('page', 1)
	limit = 10
	alamat = request.build_absolute_uri()

	context = paginasinya(serializer.data, page, limit, safe=False, alamat=alamat)
	return JsonResponse(context)

@login_required(login_url='halamanlogin_myapi')
@allowed_users(allowed_roles=['admin','mahasiswa'])
@csrf_exempt
def remove_data_mapel(request):     # remove_data_myapi
	if request.method == 'GET':
		return JsonResponse({"pesan": "harusnya method post"}, status=200)

	if request.method == 'POST':
		mapel_id = request.POST.getlist('id')
		for value in mapel_id:
			proses_hapus = Mapel.objects.get(pk=value)
			proses_hapus.delete()
			print("sukses di hapus")

		return redirect('data_mapel_myapi')

@login_required(login_url='halamanlogin_myapi')
@allowed_users(allowed_roles=['admin','mahasiswa'])
@csrf_exempt
def remove_data_arsip(request):     # remove_data_myapi
	if request.method == 'GET':
		return JsonResponse({"pesan": "harusnya method post"}, status=200)

	if request.method == 'POST':
		arsip_id = request.POST.getlist('id')
		for value in arsip_id:
			proses_hapus = Arsip.objects.get(pk=value)
			proses_hapus.delete()
			print("sukses di hapus")

		return redirect('data_mapel_myapi')

@login_required(login_url='halamanlogin_myapi')
@allowed_users(allowed_roles=['admin','mahasiswa'])
@csrf_exempt
def detail_mapel(request, id):  # name(detail_myapi)
	initialAwalMapel = {
	    "count": "",
	    "current": "",
	    "previous_page": None,
	    "next_page": False,
	    "previous": "0",
	    "next": False,
	    "total_data": "",
	    "data": [],
	    "safe": False,
	    "alamat": request.build_absolute_uri()
	}

	initialAwalArsip = {
	    "count": "",
	    "current": "",
	    "previous_page": None,
	    "next_page": False,
	    "previous": "0",
	    "next": False,
	    "total_data": "",
	    "data": [],
	    "safe": False,
	    "alamat": request.build_absolute_uri()
	}

	if request.method == 'GET':
		matapelajaran = Mapel.objects.get(pk=id)
		serializer_mapel = MapelSerializer(matapelajaran)
		try:
			data_arsip = matapelajaran.arsip_set.all()
			serializer_arsip = ArsipSerializer(data_arsip, many=True)

			# untuk paginasi
			page = request.GET.get('page', 1)
			limit = 10
			alamat = request.build_absolute_uri()
			
			context = {
				"detail_mapel": serializer_mapel.data,
				"detail_arsip": paginasinya(serializer_arsip.data, page, limit, safe=False, alamat=alamat)
			}
			
		except (ObjectDoesNotExist, AttributeError, TypeError):
			context = {
				"detail_mapel": serializer_mapel.data,
				"detail_arsip": initialAwalArsip
			}

		return JsonResponse(context)
	
	if request.method == 'POST':
		return HttpResponse('harusnya method get')

@login_required(login_url='halamanlogin_myapi')
@allowed_users(allowed_roles=['admin','mahasiswa'])
@csrf_exempt
def update_mapel(request, id):
	if request.method == 'GET':
		return HttpResponse('harusnya post')

	if request.method == 'POST':
		print('method post update mapel')
		mapel = Mapel.objects.get(pk=id)    
		mapel_form = MapelForm(request.POST or None, instance=mapel)
		if mapel_form.is_valid():
			mapel_form.save()
			print('mapel berhasil diupdate')

		return redirect('data_mapel_myapi')

@login_required(login_url='halamanlogin_myapi')
@allowed_users(allowed_roles=['admin','mahasiswa'])
@csrf_exempt
def update_arsip(request, id):
	if request.method == 'GET':
		return HttpResponse('harusnya post')

	if request.method == 'POST':
		print('method post update arsip')
		arsip = Arsip.objects.get(pk=id)    
		arsip_form = ArsipForm(request.POST or None, request.FILES, instance=arsip)
		if arsip_form.is_valid():
			arsip_form.save()
			print('arsip berhasil diupdate')

		return redirect('data_mapel_myapi')

@csrf_exempt
def absensi(request):
	if request.method == 'GET':
		db_absensi = Absensi.objects.all()
		serializer_absensi = AbsensiSerializer(db_absensi, many=True)

		# untuk paginasi
		page = request.GET.get('page', 1)
		limit = 10
		alamat = request.build_absolute_uri()
		
		context = paginasinya(serializer_absensi.data, page, limit, safe=False, alamat=alamat)
		return JsonResponse(context)

	if request.method == 'POST':
		id_mahasiswa = request.user
		get_id_kontrol_absensi = request.POST['kontrolabsensi']
		kontrol_absensi = Kontrolabsensi.objects.get(pk=get_id_kontrol_absensi)

		try:
			db_absensi = Absensi.objects.get(kontrolabsensi=get_id_kontrol_absensi, user=6) # jangan lupa digani 6 dengan id_mahasiswa
			print('sudah ada akun yang sama')
		except ObjectDoesNotExist:
			form = AbsensiForm(request.POST or None);
			if form.is_valid():
				proses_absensi = form.save(commit=False)
				proses_absensi.user = request.user.id

				if kontrol_absensi.status:
					proses_absensi.save()
					print('sukses absen')


		return redirect('absensi_myapi')

@csrf_exempt
def lihat_absensi(request):
	if request.method == 'GET':
		return HttpResponse('harusnya method post')
		
	if request.method == 'POST':
		id_mapel = request.POST['id_mapel']
		mata_pelajaran = Mapel.objects.get(pk=id_mapel)
		db_kontrolabsensi = Kontrolabsensi.objects.filter(mapel=id_mapel)
		hasil_absen = Absensi.objects.filter(kontrolabsensi__in=db_kontrolabsensi.values_list('id'))

		hasil_absensi = AbsensiSerializer(hasil_absen, many=True)
		hasil_kontrol_absensi = KontrolabsensiSerializer(db_kontrolabsensi, many=True)
		serializer_mapel = MapelSerializer(mata_pelajaran)

		# untuk paginasi
		page = request.GET.get('page', 1)
		limit = 10
		alamat = request.build_absolute_uri()
		
		context = {
			"mata_kuliah": serializer_mapel.data,
			"data_absensi": paginasinya(hasil_absensi.data, page, limit, safe=False, alamat=alamat),
			"data_kontrol": paginasinya(hasil_kontrol_absensi.data, page, limit, safe=False, alamat=alamat)
		}

		return JsonResponse(context)

@csrf_exempt
def kontrol_absensi(request):
	if request.method == 'GET':
		db_kontrolabsensi = Kontrolabsensi.objects.all()
		serializer_kontrolabsensi = KontrolabsensiSerializer(db_kontrolabsensi, many=True)

		# untuk paginasi
		page = request.GET.get('page', 1)
		limit = 10
		alamat = request.build_absolute_uri()
		
		context = paginasinya(serializer_kontrolabsensi.data, page, limit, safe=False, alamat=alamat)
		return JsonResponse(context)

	if request.method == 'POST':
		form = KontrolabsensiForm(request.POST or None);
		if form.is_valid():
			form.save()
		return redirect('kontrol_absensi_myapi')

def akun(request):
	db_user = User.objects.all()
	serializer_User = UserSerializer(db_user, many=True)

	# untuk paginasi
	page = request.GET.get('page', 1)
	limit = 10
	alamat = request.build_absolute_uri()
	
	context = paginasinya(serializer_User.data, page, limit, safe=False, alamat=alamat)
	return JsonResponse(context)

@login_required(login_url='halamanlogin_myapi')
@allowed_users(allowed_roles=['admin','mahasiswa'])
@csrf_exempt
def simulasi(request):
	print('method get simulasi')
	mapel = Mapel.objects.all()
	mapel_detail = Mapel.objects.get(pk=1)
	arsip_detail = Arsip.objects.get(pk=1)
	form = ArsipForm
	form_update_mapel = MapelForm(instance=mapel_detail)
	form_update_arsip = ArsipForm(instance=arsip_detail)

	if request.method == 'POST':
		# print('method post simulasi')
		# form = ArsipForm(request.POST, request.FILES)
		# print(form.errors)
		# print(form.is_valid())
		# if form.is_valid():
		# 	form.save()
		# 	print('sukses simpan')

		form_update_arsip = ArsipForm(request.POST, request.FILES, instance=mapel_detail)
		if form_update_arsip.is_valid():
			form_update_arsip.save()
			print('arsip sukses di update')

		return redirect('simulasi_myapi')

	context = {
		"mapel": mapel,
		"form": form,
		"form_update_arsip": form_update_arsip
	}
	# return HttpResponse('oke dong');
	return render(request, 'simulasi.html', context)
