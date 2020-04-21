f=open("allpacks.txt", "r")
contents =(f.read())
#print(contents)
f.close()
print(contents + "sai")

# li = list(contents.split(","))
# print(li)
# a=['2400','2401','2402','2404','2405','']
# print(a)
# 
# print("Missing values in second list:", (set(li).difference(a)))