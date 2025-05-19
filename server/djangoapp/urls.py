from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # ✅ Authentication APIs
    path('api/login/', views.login_user, name='login'),
    path('api/logout/', views.logout_request, name='logout'),
    path('api/register/', views.registration, name='registration'),

    # ✅ Car Make/Model API
    path('api/get_cars/', views.get_cars, name='getcars'),

    # ✅ (Future backend APIs like reviews, dealerships, etc. can be added below)
]

# ✅ Serving media files (if needed)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
