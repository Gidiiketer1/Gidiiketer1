from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gideon/", views.Gideon, name="gideon"),
    path("<str:name>/", views.greet, name="greet"),
]