import csv
with open("university_records.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    print(csv_reader[1])
     
    for line in csv_reader:
        print(line[1])