from django.urls import path
from . import views

app_name = "javaeditor"
urlpatterns = [
    path("",views.index,name="home"),
    path("compile/",views.compile,name="compiler")
]