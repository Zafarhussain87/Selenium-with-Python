import csv

arrayofdata=[[1,2,4,5,'something spam',2.334], [3,1,6,3,'anything','spam',0]]

with open("D:\java\PracticeTestCase\data\write.csv", 'w') as myfile:
    writer = csv.writer(myfile, delimiter=',', quotechar='"', quoting = csv.QUOTE_ALL)
    for row in arrayofdata:
        writer.writerow(row)
myfile.close()


read = open('D:\java\PracticeTestCase\data\write.csv','r')
reader = csv.reader(read)
for row in reader:
    print(row)