from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('resume/', views.resume, name='resume_page'),
    path('blog/', views.blog, name='blog_page'),
    path('contact/', views.contact, name='contact_page'),
    path('success/', views.success, name='success_page')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
