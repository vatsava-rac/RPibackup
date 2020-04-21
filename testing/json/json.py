import json

name1 = 'sai'
name2 = 'vatsava'
from1 = 'tenali'
from2 = 'vizag'

c={}
b={}
c['creatures']=[]
b['people']=[]
# with open("jsonuart.json", "r") as g:
#     c = json.load(g)

c['creatures'].append({
    b['people'].append({
        'name' : name1,
        'from' : from1
})
#     b['aliens']:({
#         'name' : 'asdf',
#         #'from' : from2
#     })
  })
 

# c['creatures'].append({
#     ['people'].append({
#         'name' : name2,
#         'from' : from2
#     }),
#     ['aliens'].append({
#         'name' : 'qwer',
#         'from' : 'mars'
#     })
#   })
print(c)
with open("jsonuart.json", "w") as f:
    json.dump(c,f,indent=1)