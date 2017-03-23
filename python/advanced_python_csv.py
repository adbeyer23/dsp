from advanced_python_regex import emails
import csv
file = open("emails.csv", "w")
reader = csv.reader(file)
writer = csv.writer(file)
for email in emails:
	writer.writerow([email])
  
file.close()

