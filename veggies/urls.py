from django.urls import path
from . import views

urlpatterns = [
    path('recipe/', views.recipe),
    path('<int:id>/', views.post)
]