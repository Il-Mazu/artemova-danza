from django.contrib import admin
from django.urls import include, path

from dance_school_project import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("scuole/", include("schoolmanagement.urls")),
    path("admin/", admin.site.urls),
]
