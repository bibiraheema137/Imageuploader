from django.shortcuts import render
from django.http import HttpResponse

# Home Page View
def home(request):
    return HttpResponse("Welcome to ImageUploader!")

# Upload Page View
def upload(request):
    return render(request, 'upload.html')

# Profile Page View
def profile(request):
    return render(request, 'profile.html')

# 404 Error Page View
def custom_404(request, exception):
    return render(request, '404.html', status=404)
