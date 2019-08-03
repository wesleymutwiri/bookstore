from django.urls import path
from . import views 
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home_page,name='home'),
    path('add_book', views.add_book, name='add_book'),
    path('profile', views.profile_page, name='profile_page'),
    path('explore', views.explore, name='explore'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)