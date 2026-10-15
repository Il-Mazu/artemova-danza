from django.contrib import admin
from django.urls import path

from dance_school_project import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("admin/", admin.site.urls),
]
