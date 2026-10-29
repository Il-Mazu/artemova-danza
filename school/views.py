from django.views.generic import ListView, DetailView
from school.models import DayOfTheWeek, Classroom, Course


class DayOfTheWeekListView(ListView):
    model = DayOfTheWeek


class DayOfTheWeekDetailView(DetailView):
    model = DayOfTheWeek


class ClassroomListView(ListView):
    model = Classroom


class ClassroomDetailView(DetailView):
    model = Classroom


class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course
