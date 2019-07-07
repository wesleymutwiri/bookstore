from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home_page,name='home'),
    path('add_book', views.add_book, name='add_book'),
    path('profile', views.profile_page, name='profile_page'),
    path()
]
