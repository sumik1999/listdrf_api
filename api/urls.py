from django.urls import path
from .views import RetrieveView,CreateView

urlpatterns = [
    path("",RetrieveView.as_view()),
    path("create/",CreateView.as_view())
]