from django.urls import path
from .views import generate_resume, thank_you

app_name = 'resume_generator'

urlpatterns = [
    path('generate_resume/', generate_resume, name='generate_resume'),
    path('thank_you/', thank_you, name='thank_you'),
]
