from django.contrib import admin
from django.urls import path
from imageuploader import views  # Correct Import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('upload/', views.upload, name='upload'),  # Upload page
    path('profile/', views.profile, name='profile'),  # Profile page
]

# Custom 404 Error Handler
handler404 = 'imageuploader.views.custom_404'
