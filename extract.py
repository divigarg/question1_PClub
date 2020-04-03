import re,requests, bs4
import pandas as pd

link= input("Enter the url of the website: ")
#link="https://summerofcode.withgoogle.com/archive/2019/projects/

pagedata= requests.get(link)
cleanpagedata= bs4.BeautifulSoup(pagedata.text,'html.parser')

allLists= cleanpagedata.find_all('div', class_='fixed-width')[1]
allProjects= allLists.find_all('li')



projects=[]
for i in range(len(allProjects)):
    names=allProjects[i].find_all('a')[0].get_text()
    organisationName=allProjects[i].find_all('div')[0].find_all('div')[1].get_text()
    organisations=organisationName[14:]
    project=allProjects[i].find_all('div')[0].find_all('div')[0].get_text()
    projects.append([names]+[organisations]+[project])


df= pd.DataFrame(projects, columns=['Name','Organisation','Project'])
df.to_csv('projects.csv', index=False)




