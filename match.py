from glob import glob
import csv
import json

filename= input("Enter the csv file name:")
fileJson= input("Enter the json file name:")




with open(filename, 'r',newline='', encoding="UTF-8") as inp, open("updatedName.csv",'w',newline='',encoding= "UTF-8") as out:
    readit= csv.reader(inp)
    writer=csv.DictWriter(out,quoting=csv.QUOTE_MINIMAL,fieldnames=['Name','Organisation','Project'])
    for row in readit:
        name= row[0]
        nameL= name.lower()
        count=0
        if not name.replace(" ","").isalpha():
            count=count+1
        if len(name) == 1:
            count=count+1
        if name == nameL:
            count= count+1
        if count > 0:
            print(name)
        else:
            writer.writerow({'Name':row[0],'Organisation':row[1],'Project':row[2]})
inp.close()
out.close()
print()

with open("updatedName.csv",'r',newline='', encoding="UTF-8") as csv_file, open(fileJson,'r',newline='', encoding="UTF-8")as json_file,open("matched.csv","w",newline='',encoding="UTF-8")as new:
    writing= csv.writer(new,quoting=csv.QUOTE_MINIMAL)
    writing.writerow(['Name','Roll No.','Branch','Organisation','Project'])
    csv_read= csv.reader(csv_file)
    json_read=json.load(json_file)
    for row in csv_read:
        name= row[0]
        for item in json_read:
            if name.lower()== item["n"].lower():
                print(name+", "+item["i"]+", "+item["d"]+", "+row[1]+", "+row[2])
                writing.writerow([name]+[item["i"]]+[item["d"]]+[row[1]]+[row[2]])

                

input()
