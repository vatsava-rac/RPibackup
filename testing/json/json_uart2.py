import json

#a = dict()
name1 = "SAI"
name2 = "SRI"
age1 = "25"
age2 = "24"

a={ 'name' : name1, 'age' : [age1, age2] },{'name' : name2, 'age' : age2}
a=str(a)
#b = json.dumps(a, indent=2)
#print(b)

with open("jsonuart.json", "a+") as file:
    json.dump(a,file, indent = 2)