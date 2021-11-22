from django.db import models
import json

class Schools(models.Model):
    #  mjf = my_json_file
    #  Possibly make mjf and school_data private vars
       mjf = open('/Users/alexowens/rosenwaldAlex3/Rosenwald/roseSite/static/js/school_data.json')
       school_data = json.loads(mjf.read())

class SchoolInfo(models.Model):
    school_name : str
    photo_title : str
    description : str
    publisher : str

    # for names in school_data.values():
    #     self.objects.create(school_name=names['School Names'])
    # context = {'name': self.objects.all()}

    

# Create your models here.s

