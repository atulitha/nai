import sqlite3  as db3
from res import dbconnection
import codecs
import csv

def sql_insert(con, entities):

    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO Devicelist(IPaddress, username, password) VALUES(?, ?, ?)',entities)
    
    con.commit()

con = dbconnection.sql_connection(db3)

with codecs.open('data.csv', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    #rows = [row for row in reader]
    for row in reader:
        ip,username,password=str(row[0]),str(row[1]),str(row[2])
        print (ip,username,password)
        entities = [ip,username,password]
        sql_insert(con, entities)
