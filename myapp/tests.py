# tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import UploadedImage

class ImageUploadTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_upload_image(self):
        self.client.login(username='testuser', password='password123')
        
        # Create a test image file
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")

        # Send a POST request to upload the image
        response = self.client.post(reverse('upload'), {'image': image})

        # Check if the image was uploaded successfully
        self.assertEqual(response.status_code, 302)  # Should redirect after upload
        self.assertTrue(UploadedImage.objects.exists())  # Image should be saved in the database

    def test_invalid_file_type(self):
        self.client.login(username='testuser', password='password123')
        
        # Create an invalid image file (not a JPG or PNG)
        invalid_image = SimpleUploadedFile("test_image.txt", b"file_content", content_type="text/plain")

        # Send a POST request with an invalid file type
        response = self.client.post(reverse('upload'), {'image': invalid_image})

        # Check if the error message is shown
        self.assertFormError(response, 'form', 'image', 'Invalid file type. Only JPG, JPEG, and PNG are allowed.')
