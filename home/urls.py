from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('create-admin/', views.create_admin),  # TEMPORARY
]
