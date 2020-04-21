import time
i = 0
while(1):
    i = i+1
    with open("locktest.txt", "a+") as lock1:
        lock1.write("%d" %i + "SAI\n")
        lock1.write("%d" %i + "SRI\n")
        time.sleep(1)
        lock1.write("%d" %i + "VATSAVA\n")
    