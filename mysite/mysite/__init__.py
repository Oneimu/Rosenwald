import json

# # read file
# my_json_file = open('/Users/hbcuc2-miles/rosenwald/Rosenwald/json_files/school_data.json', 'r')
# json_data = my_json_file.read()

# # parse data
# school_data = json.loads(json_data)
# print(type(school_data))


class SchoolData:
    # school_data : dict
    def __init__(self):
        # read file
        my_json_file = open('/Users/hbcuc2-miles/rosenwald/Rosenwald/json_files/school_data.json', 'r')
        json_data = my_json_file.read()

        # parse data
        self.school_data = json.loads(json_data)

    
# for key in school_data:
#     print(school_data[key]["State"])