from django.views.generic import ListView, DetailView
from schoolmanagement.models import School


class SchoolListView(ListView):
    model = School
    template_name = "schoolmanagement/school_list.html"


class SchoolDetailView(DetailView):
    model = School
    template_name = "schoolmanagement/school_detail.html"
