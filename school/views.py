from django.views.generic import ListView, DetailView
from school.models import DayOfTheWeek, Classroom


class DayOfTheWeekListView(ListView):
    model = DayOfTheWeek


class DayOfTheWeekDetailView(DetailView):
    model = DayOfTheWeek


class ClassroomListView(ListView):
    model = Classroom


class ClassroomDetailView(DetailView):
    model = Classroom
