# from django.contrib.auth.models import User, Group
from .models import *
from accounts.models import *
# from django.contrib.auth.models import User
from rest_framework import serializers

class MapelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mapel
		fields = '__all__'

class ArsipSerializer(serializers.ModelSerializer):
	class Meta:
		model = Arsip
		fields = '__all__'


class ProfilSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profil
		fields = '__all__'

class KontrolabsensiSerializer(serializers.ModelSerializer):
	class Meta:
		model = Kontrolabsensi
		fields = '__all__'

class AbsensiSerializer(serializers.ModelSerializer):
	class Meta:
		model = Absensi
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id','username']

# class LihatAbsensiSerializer(serializers.Serializer):
# 	data = serializers.CharField(max_length=200)
	