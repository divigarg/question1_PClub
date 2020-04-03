# question1_PClub

Pre-requisites: python and its libraries request, pandas and bs4 must be installed in the system
  To install the libraries 
    in windows:
      python -m pip install requests bs4 --user
      python -m pip install pandas --users


This repository contains two programs:
  1. extract.py: 
  This is a python program which asks for the input of url (eg. https://summerofcode.withgoogle.com/archive/2019/projects/) and then         creates a new file at the location of the same named "projects.csv".
  projects.csv is the data file which contains all the extracted names, corresponding organization ,corresponding project name.
  The file  is printed in the following format:
        Name1, Organisation1, Project1
        Name2, Organisation2, Project2
        Name3, Organisation3, Project3
        ...
  
  2. match.py: 
  This is a python program which first asks for the address or if in the same folder name for the csv file.The csv file you have to enter 
  is the filename with extension also. The csv file is of the same format as created in the program extrat.py
  Now second Time it asks for a json file address with extension (which provide in the question was students.json)
  After that it find names in the csv file that do not look like official names and print them. The rules for checking non-official names     are:
    1) The name contains any of the special symbols or numbers.
    2) The name consists of only one word.
    3) The name contains only lowercase letters.   
   Then the remaining names (that are official names) are matched against the JSON file. Then the program prints (to stdout) the details of    all the names that are present both in the JSON file and in the CSV file, in the following format:
   Name(common to both JSON and CSV), Roll No(from JSON), Branch(from JSON), Organisation(from CSV), Project(from CSV)
