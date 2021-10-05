from django.shortcuts import render
from .models import SchoolData


def index(request):
    schools = SchoolData()
    data = schools.school_data
    #change school name to a dict and remove the check for empty strings
    school_names = []
    for school in data:
        if data[school]["School Names"] not in school_names and data[school]["School Names"] != "":
            school_names.append(data[school]["School Names"])

    return render(request, 'index.html', {'names': school_names})


# Create your views here
