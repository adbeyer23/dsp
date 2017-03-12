import pandas as pd
faculty = pd.read_csv("faculty.csv")
faculty = faculty.rename(columns = lambda x: x.strip())
faculty["degree"] = faculty["degree"].apply(lambda x: x.replace(".", ""))
faculty["degree"] = faculty["degree"].apply(lambda x: x.strip())
faculty["degree"] = faculty["degree"].apply(lambda x: x.split())
degrees = list(faculty.degree)
from collections import Counter
degrees_fixed = []
for x in degrees:
    for y in x:
        degrees_fixed.append(y)
Counter(degrees_fixed)
faculty.set_value(24,  "title", "Assistant Professor of Biostatistics")

emails = list(faculty.email)

email_domains = [x.split("@")[-1] for x in emails]
from collections import Counter
Counter(email_domains)


