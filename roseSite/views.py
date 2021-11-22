from django.shortcuts import render
from django.http import HttpResponse
from .models import SchoolInfo, Schools
import json
import random

'''
Eventually we are going to have to send the pictures to the front by 
using the picture ID

This code is a bit much but will be optimized once the frontend makes it convient for 
the data to be pushed through a simple for loop

The school names change everytime we refresh the page. 
Should it be static or keep it as it is?

'''
def index(request):

    schools = Schools().school_data
    schools1 = SchoolInfo()
    schools2 = SchoolInfo()
    schools3 = SchoolInfo()
    schools4 = SchoolInfo()
    schools5 = SchoolInfo()
    schools6 = SchoolInfo()

    i = 0
    s_names = set()
    # all unti

    for names in schools.values():
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

def results(request):
    pass
# Create your views here.

