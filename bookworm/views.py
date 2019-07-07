from django.shortcuts import render, redirect
from . import forms
from . import models

def home_page(request):
	return render(request, 'bookstore/home.html')

def category_page(request):
	return render(request, 'bookstore/category_page.html')

def add_book(request):
	if request.method == 'POST':
		form = BookForm(request.POST, request.FILES)
		if form.is_valid():
			books = form.save(commit=False)
			books.save()
			return redirect('home_page')
	else:
		form = BookForm()

	return render(request, 'bookstore/upload.html', {"form":form})

def profile_page(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.save()
			return redirect('profile_page')
		else:
			form = ProfileForm()
	return render(request, 'bookstore/profile.html')

def explore(request):
	return render(request,'bookstore/explore.html')	