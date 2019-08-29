from bs4 import BeautifulSoup as bs
import lxml
import requests
import os

page = requests.get("https://www.acm.org/chapters/find-a-chapter")
soup = bs(page.text,'lxml')
text = soup.select("script")

k = str(text)
k = k.split('<script type="text/javascript">')
k = k[2]
k = k.split('/*')
k = k[0]
k = k.split('[')
k = k[2:]

file = 'Chapters.csv'

with open(file,"a") as myfile:
    myfile.write("COLLEGE,COUNTRY,DATE OF ESTB, YEAR OF ESTB,TYPE OF CHAPTER,EMAIL,CONTACT,CHAIR\n")
    for a in k:
        b = a.split(']')
        b = b[0]
        b = b.split('"')
        #b1=college,#b19=country,#b21=dateofestablish,#b23=type,#b29=email,#b31=contact,#b39=chairName
        try:        
            d = b[1].split(',')
            b[1] = d[0] + " " + d[1]
            c = b[1] + ',' + b[19] + ',' + b[21] + ',' + b[23] + ',' + b[29] + ',' + b[31] + ',' + b[39] + '\n'
            myfile.write(c)
        except:
            try:
                d = b[31].split(',')
                b[31] = d[0] + d[1]
                c = b[1] + ',' + b[19] + ',' + b[21] + ',' + b[23] + ',' + b[29] + ',' + b[31] + ',' + b[39] + '\n'
                myfile.write(c)
            except:
                c = b[1] + ',' + b[19] + ',' + b[21] + ',' + b[23] + ',' + b[29] + ',' + b[31] + ',' + b[39] + '\n'
                myfile.write(c)


  