from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, register, user_login, user_logout, profile, upload_image, gallery

urlpatterns = [
    path('', home, name='home'),  # Home Page
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('upload/', upload_image, name='upload'),
    path('gallery/', gallery, name='gallery'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
