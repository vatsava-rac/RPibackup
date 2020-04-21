with open("listTest1.txt", 'r') as li:
    list_1 = li.read()
    
list_1_1 = list_1.split("\n")
print(list_1_1)

a = list_1_1.remove('RACEA03A002')
print(list_1_1)
print(a)

list_1_1.sort()
print(list_1_1)

with open("listTest1.txt", 'w') as lil:
    for item in list_1_1:
        lil.write("%s\n" %item)
