import json

name1 = "SAI"
name2 = "SRI"
age1 = "25"
age2 = "24"

me = {"name" : [name1, name2], "age" : [age1, age2]}

#print(me)

a = json.dumps(me, indent =2)
print(a)

with open("jsonmain.json", "w") as jos:
    jos.write(a)