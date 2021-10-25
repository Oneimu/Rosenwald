from django.shortcuts import render
from django.http import HttpResponse
from .models import SchoolNames
import json
import random

def index(request):
    schools1 = SchoolNames()
    schools2 = SchoolNames()
    schools3 = SchoolNames()
    schools4 = SchoolNames()
    schools5 = SchoolNames()
    schools6 = SchoolNames()
    my_json_file = open('/Users/hbcuc2-miles/rosenwal/roseSite/static/js/school_data.json')
    school_data = json.loads(my_json_file.read())
    i = 0
    s_names = set()
    # all unti

    for names in school_data.values():
        s_names.add(names['School Names'])

    for name in s_names:
        if i == 1:
            schools1.school_name = name
        elif i == 2:
            schools2.school_name = name
        elif i == 3:
            schools3.school_name = name
        elif i == 4:
            schools4.school_name = name
        elif i == 5:
            schools5.school_name = name
        elif i == 6:
            schools6.school_name = name
        elif i == 7: break
        i += 1



    # schools = [schools1, schools2, schools3]
    #     school_names.objects.create(school_name=names['School Names'])
    # context = {'name': school_names.objects.all()}
    return render(request, 'index.html', {'school1': schools1, 'school2': schools2, 'school3': schools3, 'school4': schools4, 'school5': schools5, 'school6': schools6})

# Create your views here.

