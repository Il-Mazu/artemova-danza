from django.urls import path
from school import views

urlpatterns = [
    path("giorni/", views.DayOfTheWeekListView.as_view(), name="dayoftheweek_list"),
    path("giorni/<int:pk>/", views.DayOfTheWeekDetailView.as_view(), name="dayoftheweek_detail"),
    path("giorni/nuovo/", views.DayOfTheWeekCreateView.as_view(), name="dayoftheweek_create"),
    path("giorni/<int:pk>/modifica/", views.DayOfTheWeekUpdateView.as_view(), name="dayoftheweek_update"),
    path("aule/", views.ClassroomListView.as_view(), name="classroom_list"),
    path("aule/<int:pk>/", views.ClassroomDetailView.as_view(), name="classroom_detail"),
    path("aule/nuova/", views.ClassroomCreateView.as_view(), name="classroom_create"),
    path("aule/<int:pk>/modifica/", views.ClassroomUpdateView.as_view(), name="classroom_update"),
    path("aule/<int:pk>/elimina/", views.ClassroomDeleteView.as_view(), name="classroom_delete"),
    path("", views.CourseListView.as_view(), name="course_list"),
    path("<int:pk>/", views.CourseDetailView.as_view(), name="course_detail"),
    path("nuovo/", views.CourseCreateView.as_view(), name="course_create"),
    path("<int:pk>/modifica/", views.CourseUpdateView.as_view(), name="course_update"),
    path("<int:pk>/elimina/", views.CourseDeleteView.as_view(), name="course_delete"),
]
