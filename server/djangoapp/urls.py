# Uncommented imports
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # API route for backend login POST request
    path('api/login/', views.login_user, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('register', views.registration, name='registration'),

    # (Future backend APIs like registration, logout, etc. can be added here)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
