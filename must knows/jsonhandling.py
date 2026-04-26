import json

# from json string to python obj - dict
json_string = '{"name": "satya", "age": 22}'
dict = json.loads(json_string)
print(dict)

# from python obj - dict to json string
dict = {
    "name"  : "satya",
    "age"   : 22
}
json_string = json.dumps(dict)
print(json_string)

# we can convert dict, lis, tuple, string, int, float, True, False, None
print(json.dumps(43))
print(json.dumps(False))

"""
python objs -> JSON equivalents (js)
"""

# indent to define no of indents
print(json.dumps(dict, indent = 4))

# to change default separator
print(json.dumps(dict, indent = 4, separators = (".", "=")))

# write to a file
with open("data.json", "w") as f:
    json.dump(dict, f, indent = 2)

# read from file
with open('data.json', 'r') as f:
    loaded = json.load(f)
    print(loaded)