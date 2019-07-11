from django.urls import path
from . import views 
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('',views.home_page,name='home'),
    path('add_book', views.add_book, name='add_book'),
    path('profile', views.profile_page, name='profile_page'),
    path('explore', views.explore, name='explore'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
