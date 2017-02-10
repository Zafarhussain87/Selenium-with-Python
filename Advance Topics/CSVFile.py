import csv

file = open('D:\java\PracticeTestCase\data\CSV.csv', 'r')
reader = csv.reader(file)
for row in reader:
    print (row)

file.close()