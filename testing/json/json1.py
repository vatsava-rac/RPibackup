import json

name1 = 'sai'
name2 = 'vatsava'
from1 = 'tenali'
from2 = 'vizag'
b = {}
b['people']=[]
b['aliens']=[]

with open("jsonuart1.json", "r") as g:
    b = json.load(g)

b['people'].append({
    'name' : name1,
    'from' : from1
    })
# b['aliens'].append({
#     'name' : 'asdf',
#     'from' : 'venus'
#     })

# b['people'].append({
#      'name' : name2,
#     'from' : from2
#     }),
# b['aliens'].append({
#     'name' : 'qwer',
#      'from' : 'mars'
#     })

print(b)
with open("jsonuart1.json", "a+") as f:
    json.dump(b,f,indent=1)
