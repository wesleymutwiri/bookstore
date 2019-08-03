from django.shortcuts import render, redirect
from .forms import BookForm, ProfileForm
from .models import Book, Profile, Category
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

def home_page(request):
	books = Book.objects.all
	return render(request, 'bookstore/home.html', {"books":books})

def category_page(request):
	return render(request, 'bookstore/category_page.html')

def add_book(request):
	if request.method == 'POST':
		form = BookForm(request.POST, request.FILES)
		if form.is_valid():
			books = form.save(commit=False)
			books.save()
			return redirect('home')
	else:
		form = BookForm()

	return render(request, 'bookstore/upload.html', {"form":form})

def profile_page(request):
	# user = User.get_current user
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.save()
			return redirect('profile_page')
	else:
		form = ProfileForm()
	return render(request, 'bookstore/profile.html', {"form":form})

def explore(request):
	return render(request,'bookstore/explore.html')	

class RegisterView(CreateView):
	template_name = 'registration/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('home')