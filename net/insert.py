from res import dbconnection
import sqlite3 as db3
def sql_insert(con, entities):

    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO Devicelist(IPaddress, username, password) VALUES(?, ?, ?)', entities)
    
    con.commit()

entities = ()

con = dbconnection.sql_connection(db3)

sql_insert(con, entities)
