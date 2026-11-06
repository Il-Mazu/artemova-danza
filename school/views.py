from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from school.models import DayOfTheWeek, Classroom, Course


class DayOfTheWeekListView(ListView):
    model = DayOfTheWeek


class DayOfTheWeekDetailView(DetailView):
    model = DayOfTheWeek


class DayOfTheWeekCreateView(CreateView):
    model = DayOfTheWeek
    fields = ["number", "name"]
    success_url = reverse_lazy("dayoftheweek_list")


class DayOfTheWeekUpdateView(UpdateView):
    model = DayOfTheWeek
    fields = ["number", "name"]

    def get_success_url(self):
        return reverse_lazy("dayoftheweek_detail", kwargs={"pk": self.object.pk})


class ClassroomListView(ListView):
    model = Classroom


class ClassroomDetailView(DetailView):
    model = Classroom


class ClassroomCreateView(CreateView):
    model = Classroom
    fields = ["name", "capacity"]
    success_url = reverse_lazy("classroom_list")


class ClassroomUpdateView(UpdateView):
    model = Classroom
    fields = ["name", "capacity"]

    def get_success_url(self):
        return reverse_lazy("classroom_detail", kwargs={"pk": self.object.pk})


class ClassroomDeleteView(DeleteView):
    model = Classroom
    success_url = reverse_lazy("classroom_list")


class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course


class CourseCreateView(CreateView):
    model = Course
    fields = ["subject", "day_of_the_week", "starting_hour", "classroom", "school"]
    success_url = reverse_lazy("course_list")


class CourseUpdateView(UpdateView):
    model = Course
    fields = ["subject", "day_of_the_week", "starting_hour", "classroom", "school"]

    def get_success_url(self):
        return reverse_lazy("course_detail", kwargs={"pk": self.object.pk})


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy("course_list")
