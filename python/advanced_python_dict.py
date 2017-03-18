import csv

#Q7
with open('faculty.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    fac_dict = dict()
    keys_list = []
    
    for row in reader:
        key = row["name"].split(" ")[-1]
        if key in fac_dict.keys():
            fac_dict[key].append([row[" title"].strip(), row[" degree"].strip(), row[" email"].strip()])
            
        else:    
            fac_dict[key] = [[row[" title"].strip(), row[" degree"].strip(), row[" email"].strip()]]
      
    count = 0
    for key, value in fac_dict.items():
        if count <= 2:
          print ("{}: {}".format(key,fac_dict[key]))
          count +=1
    
#Q8
with open('faculty.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    fac_dict = {}

    for row in reader:
        key = (row["name"].split()[0], row["name"].split()[-1])
        value = [row[" title"].strip(), row[" degree"].strip(), row[" email"].strip()]
        fac_dict[key] = value

    count = 0
    for key, value in fac_dict.items():
        print ("{}: {}".format(key,fac_dict[key]))
        count += 1
            

#Q9
for key in sorted(fac_dict.keys(), key = lambda x: x[1]):
    print ("{}: {}".format(key,fac_dict[key]))
