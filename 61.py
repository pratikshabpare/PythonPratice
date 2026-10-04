# Student ={
#     "name" :"Pratiksha",
#     "age" : 23,
#     "course ": "MCA"
# }
# print(Student)
# Student["age"]=24
# print(Student)
# del Student["age"]
# print(Student)
# Count the frequency
# text="hello"
# frequency={}
# for ch in text:
#     if ch in frequency:
#         frequency[ch] +=1 
#     else:
#         frequency[ch] = 1
# print(frequency)
marks={
    "Java":80,
    "Python":90,
    "SQL":75,
    "Angular":85
}
highest_key=""
highest_value=0
for key in marks:
    if marks[key] > highest_value:
        highest_value=marks[key]
print()