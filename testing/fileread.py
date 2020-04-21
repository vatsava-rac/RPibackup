with open("filetest.txt", "r") as f:
    a = f.read()
    
print(type(a))
print(a)

b = a.split("\n")
print(b)
print(b[0])
print(type(b[0]))
print(len(b))