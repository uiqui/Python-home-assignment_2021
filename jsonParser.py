import json

path = '../configClear_v2.json'
#pathFix = '../configClear_v2_fix.json'

file = open(path, 'r')

data = json.load(file)

file.close()

#with open(path, "r") as json_file:
#    data = json.load(json_file)
