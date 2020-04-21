import json

name1 = "SAI"
name2 = "SRI"
age1 = "23"
age2 = "24"
num1 = "1234"
num2 = "5678"
a = {}
for i in range (2):
    a["name" + str(1+i)] = name1
    
a["num"] = {"num1" : num1, "num2" : num2}

a["num"] = "f"
a["num"]["num1"] = num1
a["num"]["num2"] = num2

b = json.dumps(a, indent = 2)
print(type(a))
    
print(b)