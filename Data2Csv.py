import csv

fileptr = open("/Users/rehmanmasood/Documents/GitHub/er_wait_times/data/Timely_and_Effective_Care_-_Hospital.csv", "r")
lines = fileptr.readlines()
data = csv.DictReader(lines)
print ("CREATE TABLE Measures (ID INT(10), Provider_ID INT(10), Hospital_Name VARCHAR(80), Address VARCHAR(200), City VARCHAR(80), State VARCHAR(2), Zip_Code INT(9), County_Name VARCHAR(20), Phone_Number INT(10), Condition VARCHAR(200), Measure_ID VARCHAR(20), Measure_Name VARCHAR(200), Score VARCHAR(40), Sample VARCHAR(200), Footnote VARCHAR(200), Measure_Start_Date DATETIME, Measure_End_Date DATETIME, Longitude FLOAT(20), Latitude FLOAT(20));")
for d in data:
    Longitude = ""
    Latitude = ""
    LongitudeLatitude = d["Location"].split("\n")[2]
    if LongitudeLatitude != "":
        Longitude = LongitudeLatitude.split(",")[0].strip().replace("(", "")
        Latitude = LongitudeLatitude.split(",")[1].strip().replace(")", "")
    print ("INSERT INTO Measures (Provider_ID, Hospital_Name, Address, City, State, Zip_Code, County_Name, Phone_Number, Condition, Measure_ID, Measure_Name, Score, Sample, Footnote, Measure_Start_Date, Measure_End_Date, Longtitude, Latitude) VALUES ({0}, \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\", \"{6}\", \"{7}\", \"{8}\", \"{9}\", \"{10}\", \"{11}\", \"{12}\", \"{13}\");".format(d["Provider ID"], d["Hospital Name"], d["Address"], d["City"], d["State"], d["ZIP Code"], d["County Name"], d["Phone Number"], d["Condition"], d["Footnote"], d["Measure Start Date"], d["Measure End Date"], Longitude, Latitude))
fileptr.close()
