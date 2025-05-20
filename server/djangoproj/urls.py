from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),  # Backend APIs
    path('register/', TemplateView.as_view(template_name="index.html")),
    path('dealers/', TemplateView.as_view(template_name="index.html")),

    # Frontend routes handled by React build
    re_path(r'^.*$', TemplateView.as_view(template_name="index.html")),
]
