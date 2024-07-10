from django.urls import path
from .views import save_question
urlpatterns = [
    path('my_page/user_question/', save_question, name = 'save question')
]