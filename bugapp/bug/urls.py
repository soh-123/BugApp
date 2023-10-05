from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path('register/', views.register_bug, name="register bug"),
    path('<int:bug_id>/', views.bug_details, name='bug details'),
]
