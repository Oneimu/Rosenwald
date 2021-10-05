from django.shortcuts import render
from .models import SchoolData


def index(request):
    schools = SchoolData()
    data = schools.school_data
    #change school name to a dict 
    school_names = []
    for school in data:
        if data[school]["School Names"] not in school_names:
            school_names.append(data[school]["School Names"])

    return render(request, 'index.html', {'school_names': school_names})


# Create your views here
