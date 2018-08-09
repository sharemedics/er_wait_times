import csv
import mysql.connector

fileptr = open("/Users/rehmanmasood/Documents/GitHub/er_wait_times/data/Timely_and_Effective_Care_-_Hospital.csv", "r")
lines = fileptr.readlines()
data = csv.DictReader(lines)
for d in data:
        print (d['Measure ID'])
fileptr.close()
