# Advanced Python    

### Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

### Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

Counter({'0': 1,
         'BSEd': 1,
         'JD': 1,
         'MA': 1,
         'MD': 1,
         'MPH': 2,
         'MS': 2,
         'PhD': 31,
         'ScD': 6})
8 total degrees (and one person possibly without one).

#### Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

Professor of Biostatistics              13. 
Assistant Professor of Biostatistics    12. 
Associate Professor of Biostatistics    12. 
#### Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu', 'sellenbe@upenn.edu', 'jellenbe@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu', 'pgimotty@upenn.edu', 'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu', 'rhubb@mail.med.upenn.edu', 'whwang@mail.med.upenn.edu', 'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'liy3@email.chop.edu', 'mingyao@mail.med.upenn.edu', 'hongzhe@upenn.edu', 'rlocalio@upenn.edu', 'nanditam@mail.med.upenn.edu', 'knashawn@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu', 'michross@upenn.edu', 'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'shawp@upenn.edu', 'rshi@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu', 'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu', 'atroxel@mail.med.upenn.edu', 'rxiao@mail.med.upenn.edu', 'sxie@mail.med.upenn.edu', 'dxie@upenn.edu', 'weiyang@mail.med.upenn.edu']

#### Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

Counter({'cceb.med.upenn.edu': 1,
         'email.chop.edu': 1,
         'mail.med.upenn.edu': 23,
         'upenn.edu': 12})



Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

### Part II - Write to CSV File

#### Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

#### Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

Ross: [['Assistant Professor is Biostatistics', 'PhD', 'michross@upenn.edu']]
Bilker: [['Professor of Biostatistics', 'Ph.D.', 'warren@upenn.edu']]
Bryan: [['Assistant Professor of Biostatistics', 'PhD', 'bryanma@upenn.edu']]

#### Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:

('Hongzhe', 'Li'): ['Professor of Biostatistics', 'Ph.D', 'hongzhe@upenn.edu']
('Dawei', 'Xie'): ['Assistant Professor of Biostatistics', 'PhD', 'dxie@upenn.edu']
('Knashawn', 'Morales'): ['Associate Professor of Biostatistics', 'Sc.D.', 'knashawn@mail.med.upenn.edu']

#### Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

('Scarlett', 'Bellamy'): ['Associate Professor of Biostatistics', 'Sc.D.', 'bellamys@mail.med.upenn.edu']
('Warren', 'Bilker'): ['Professor of Biostatistics', 'Ph.D.', 'warren@upenn.edu']
('Matthew', 'Bryan'): ['Assistant Professor of Biostatistics', 'PhD', 'bryanma@upenn.edu']
('Jinbo', 'Chen'): ['Associate Professor of Biostatistics', 'Ph.D.', 'jinboche@upenn.edu']
('Jonas', 'Ellenberg'): ['Professor of Biostatistics', 'Ph.D.', 'jellenbe@mail.med.upenn.edu']
('Susan', 'Ellenberg'): ['Professor of Biostatistics', 'Ph.D.', 'sellenbe@upenn.edu']
('Rui', 'Feng'): ['Assistant Professor of Biostatistics', 'Ph.D', 'ruifeng@upenn.edu']
('Benjamin', 'French'): ['Associate Professor of Biostatistics', 'PhD', 'bcfrench@mail.med.upenn.edu']
('Phyllis', 'Gimotty'): ['Professor of Biostatistics', 'Ph.D', 'pgimotty@upenn.edu']
('Wensheng', 'Guo'): ['Professor of Biostatistics', 'Ph.D', 'wguo@mail.med.upenn.edu']
('Yenchih', 'Hsu'): ['Assistant Professor of Biostatistics', 'Ph.D.', 'hsu9@mail.med.upenn.edu']
('Rebecca', 'Hubbard'): ['Associate Professor of Biostatistics', 'PhD', 'rhubb@mail.med.upenn.edu']
('Wei-Ting', 'Hwang'): ['Associate Professor of Biostatistics', 'Ph.D.', 'whwang@mail.med.upenn.edu']
('Marshall', 'Joffe'): ['Professor of Biostatistics', 'MD MPH Ph.D', 'mjoffe@mail.med.upenn.edu']
('J.', 'Landis'): ['Professor of Biostatistics', 'B.S.Ed. M.S. Ph.D.', 'jrlandis@mail.med.upenn.edu']
('Hongzhe', 'Li'): ['Professor of Biostatistics', 'Ph.D', 'hongzhe@upenn.edu']
('Mingyao', 'Li'): ['Associate Professor of Biostatistics', 'Ph.D.', 'mingyao@mail.med.upenn.edu']
('Yimei', 'Li'): ['Assistant Professor of Biostatistics', 'Ph.D.', 'liy3@email.chop.edu']
('A.', 'Localio'): ['Associate Professor of Biostatistics', 'JD MA MPH MS PhD', 'rlocalio@upenn.edu']
('Nandita', 'Mitra'): ['Associate Professor of Biostatistics', 'Ph.D.', 'nanditam@mail.med.upenn.edu']
('Knashawn', 'Morales'): ['Associate Professor of Biostatistics', 'Sc.D.', 'knashawn@mail.med.upenn.edu']
('Kathleen', 'Propert'): ['Professor of Biostatistics', 'Sc.D.', 'propert@mail.med.upenn.edu']
('Mary', 'Putt'): ['Professor of Biostatistics', 'PhD ScD', 'mputt@mail.med.upenn.edu']
('Sarah', 'Ratcliffe'): ['Associate Professor of Biostatistics', 'Ph.D.', 'sratclif@upenn.edu']
('Michelle', 'Ross'): ['Assistant Professor is Biostatistics', 'PhD', 'michross@upenn.edu']
('Jason', 'Roy'): ['Associate Professor of Biostatistics', 'Ph.D.', 'jaroy@mail.med.upenn.edu']
('Mary', 'Sammel'): ['Professor of Biostatistics', 'Sc.D.', 'msammel@cceb.med.upenn.edu']
('Pamela', 'Shaw'): ['Assistant Professor of Biostatistics', 'PhD', 'shawp@upenn.edu']
('Russell', 'Shinohara'): ['Assistant Professor of Biostatistics', '0', 'rshi@mail.med.upenn.edu']
('Haochang', 'Shou'): ['Assistant Professor of Biostatistics', 'Ph.D.', 'hshou@mail.med.upenn.edu']
('Justine', 'Shults'): ['Professor of Biostatistics', 'Ph.D.', 'jshults@mail.med.upenn.edu']
('Alisa', 'Stephens'): ['Assistant Professor of Biostatistics', 'Ph.D.', 'alisaste@mail.med.upenn.edu']
('Andrea', 'Troxel'): ['Professor of Biostatistics', 'ScD', 'atroxel@mail.med.upenn.edu']
('Rui', 'Xiao'): ['Assistant Professor of Biostatistics', 'PhD', 'rxiao@mail.med.upenn.edu']
('Dawei', 'Xie'): ['Assistant Professor of Biostatistics', 'PhD', 'dxie@upenn.edu']
('Sharon', 'Xie'): ['Associate Professor of Biostatistics', 'Ph.D.', 'sxie@mail.med.upenn.edu']
('Wei', 'Yang'): ['Assistant Professor of Biostatistics', 'Ph.D.', 'weiyang@mail.med.upenn.edu']

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

