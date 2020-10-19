import csv
with open('titanic.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    counter = 0
    for row in reader:
        counter += 1
    print counter
