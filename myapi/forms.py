from django.forms import ModelForm
from myapi.models import *
from accounts.models import *

class ArsipForm(ModelForm):
	class Meta:
		model = Arsip
		fields = '__all__'

class MapelForm(ModelForm):
	class Meta:
		model = Mapel
		fields = '__all__'

class ProfilForm(ModelForm):
	class Meta:
		model = Profil
		fields = '__all__'

class AbsensiForm(ModelForm):
	class Meta:
		model = Absensi
		fields = '__all__'

class KontrolabsensiForm(ModelForm):
	class Meta:
		model = Kontrolabsensi
		fields = '__all__'