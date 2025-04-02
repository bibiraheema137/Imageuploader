from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import UploadedImage
from .forms import ImageUploadForm, UserRegisterForm

# Home Page
def home(request):
    return render(request, 'homepage.html')

# User Registration
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)  # Encrypt password
            user.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# User Login
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

# User Logout
def user_logout(request):
    logout(request)
    return redirect('login')

# User Profile & Image Upload
@login_required
def profile(request):
    images = UploadedImage.objects.filter(user=request.user)
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save(commit=False)
            uploaded_image.user = request.user
            uploaded_image.save()
            return redirect('profile')
    else:
        form = ImageUploadForm()
    return render(request, 'profile.html', {'form': form, 'images': images})

# Upload Image
@login_required
def upload_image(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save(commit=False)
            uploaded_image.user = request.user
            uploaded_image.save()
            return redirect('profile')
    return render(request, 'upload.html', {'form': ImageUploadForm()})

# Gallery Page (All Uploaded Images)
@login_required
def gallery(request):
    images = UploadedImage.objects.all()
    return render(request, 'gallery.html', {'images': images})
