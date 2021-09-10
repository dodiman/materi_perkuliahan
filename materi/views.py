from django.shortcuts import render, redirect
from accounts.decorators import unauthenticated_user, allowed_users, admin_only
from accounts.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


@login_required(login_url='halamanlogin_myapi')
@allowed_users(allowed_roles=['admin','mahasiswa'])
def index(request):
	return render(request, 'index.html')

def logoutPage(request):
	logout(request)
	return redirect('login_index')

@unauthenticated_user
def loginPage(request):
	form = LoginForm()
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('mydata_myapi')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {"form": form}
	return render(request, 'login.html', context)

@unauthenticated_user
def register(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		print(form.errors)
		print(form.is_valid())
		if form.is_valid():
			user = form.save()
			print('sukses daftar')
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='mahasiswa')
			user.groups.add(group)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login_index')
		

	context = {'form':form}
	return render(request, 'register.html', context)