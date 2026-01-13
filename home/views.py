from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def create_render_admin(request):
    username = "admin"
    email = "dilaraucar.t@gmail.com"
    password = "StrongPassword123!"

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        return HttpResponse("✅ Superuser created. REMOVE THIS VIEW NOW.")
    else:
        return HttpResponse("⚠️ Superuser already exists. REMOVE THIS VIEW NOW.")