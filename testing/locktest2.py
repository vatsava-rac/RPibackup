import time
i = 0
while(1):
    with open("locktest.txt", "a+") as file:
        i = i+1
        file.write("%d " %i + "testing1\r\n")
        file.write("%d " %i + "testing2\r\n")
        time.sleep(3)
        file.write("%d " %i + "testing3\r\n")