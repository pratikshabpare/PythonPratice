import json
student={
    "name":"Pratiksha",
    "age":22,
    
}
json_data=json.dumps(student)
print(json_data)
print(type(json_data))