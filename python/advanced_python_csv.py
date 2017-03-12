from advanced_python_regex import emails
import cvs
file = open("emails.csv", "rb")
reader = csv.reader(file)
writer = csv.writer(file)
for email in emails:
  writer.writerow(email)
file.close()
