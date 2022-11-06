import requests
import json
import mysql.connector

try:
     mydb = mysql.connector.connect(host = 'localhost',user ='root',password ='',database = 'entriesapidb')
except mysql.connector.Error as e :
    print("error in mysql connection")
mycursor = mydb.cursor()
data = requests.get("https://api.publicapis.org/entries").text
data_info = json.loads(data)
for i in data_info['entries']:
    try:
        #sql = "INSERT INTO `entriesfetch`(`api`, `description`, `auth`, `https`, `cors`, `link`, `category`) VALUES ('"+i['API']+"','"+i['Description']+"','"+i['Auth']+"','"+i['HTTPS']+"','"+i['Cors']+"','"+i['Link']+"','"+i['Category']+"')"   
        sql = "INSERT INTO `entries`(`api`, `description`, `auth`, `https`, `cors`, `link`, `category`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
   
        data=(i['API'],i['Description'],i['Auth'],i['HTTPS'],i['Cors'],i['Link'],i['Category'])
    
        mycursor.execute(sql,data)
        mydb.commit()
    except mysql.connector.Error as e:
        print("error in insertion",e)
    print("data inserted successfully!",i['API'])