# Create your views here.
from django.shortcuts import render

def social_login_view(request):
    return render(request, 'login.html')