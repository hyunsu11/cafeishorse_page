
from django.urls import path, include
from .views import helloAPI, randomQuiz, byeAPI

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),
    path("bye/", byeAPI),
]