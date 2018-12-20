import json
import sys

def parse_json(location, top_level_json, child_level_json, key):

   with open(location) as f:
       json_data = json.load(f)
       print(json_data)
   
       for line in json_data[top_level_json][child_level_json]:
           print(str(line[key]))
           
location = sys.argv[1]
top_level_json = sys.argv[2]
child_level_json = sys.argv[3]
key = sys.argv[4]

parse_json(location, top_level_json, child_level_json, key)
