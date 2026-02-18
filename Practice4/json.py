import json

data = {
    "name": "Tamerlan",
    "age": 17,
    "is_student": True
}

json_string = json.dumps(data)

print(json_string)
print(type(json_string))
