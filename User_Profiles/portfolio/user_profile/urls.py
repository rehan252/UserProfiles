from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'user_profile'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change-password', views.change_password, name='change-password')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
