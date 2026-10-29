from django.urls import path
from school import views

urlpatterns = [
    path("giorni/", views.DayOfTheWeekListView.as_view(), name="dayoftheweek_list"),
    path("giorni/<int:pk>/", views.DayOfTheWeekDetailView.as_view(), name="dayoftheweek_detail"),
    path("aule/", views.ClassroomListView.as_view(), name="classroom_list"),
    path("aule/<int:pk>/", views.ClassroomDetailView.as_view(), name="classroom_detail"),
    path("", views.CourseListView.as_view(), name="course_list"),
    path("<int:pk>/", views.CourseDetailView.as_view(), name="course_detail"),
]
