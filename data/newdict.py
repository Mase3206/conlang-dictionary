import csv

fileName = input("What is the name of the CSV file? Include the file extension. (case sensitive)\n")
dictLang = input("What is the non-English language of the dictionary?")

with open(fileName, newline='') as csvfile:
    csvDict = csv.writer(csvfile, dialect='unix')
    csvDict.writerow(['Dictionary Language', dictLang])

