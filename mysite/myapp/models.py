from django.db import models
import json

class SchoolData:
    # school_data : dict
    def __init__(self):
        # read file
        my_json_file = open('/Users/hbcuc2-miles/rosenwald/Rosenwald/json_files/school_data.json', 'r')
        json_data = my_json_file.read()

        # parse data
        self.school_data = json.loads(json_data)
# Create your models here.
