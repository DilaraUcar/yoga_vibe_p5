from django.shortcuts import render

from django.contrib.auth.models import User
from django.http import HttpResponse


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="YourSecurePassword123!"
        )
        return HttpResponse("Superuser created!")
    return HttpResponse("Superuser already exists!")
