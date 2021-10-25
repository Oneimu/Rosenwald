from django.db import models
import json

class SchoolNames(models.Model):
    school_name : str
    # my_json_file = open('/Users/hbcuc2-miles/rosenwal/roseSite/static/js/school_data.json')
    # school_data = json.loads(my_json_file.read())
    # for names in school_data.values():
    #     self.objects.create(school_name=names['School Names'])
    # context = {'name': self.objects.all()}

    

# Create your models here.
