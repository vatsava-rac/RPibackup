import json

b = {"name": "John", "age": [{"age1":30,"age2":60}]}
c = json.dumps(b, indent = 2)
print(type(b["name"]))

pep = {"people" :
 [{
     "name" : "SAI",
     "age" : 23
     },
 {
     "name" : "SRI",
     "age" : 24
     }]
 }
print(type(pep))
pepp = json.dumps(pep, indent = 2)
print(pepp)

lam = pepp.loads(pepp)
lam.append({
    "name" : "VATSAVA",
    "age" : 25
    }
    )
print(pepp)



