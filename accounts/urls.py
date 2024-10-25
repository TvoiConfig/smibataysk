from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.registration, name='reg'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)