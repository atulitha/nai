import sqlite3 as db3
import dbconnection
def sql_table(con):
    cursorObj = con.cursor()
    try:
        cursorObj.execute("CREATE TABLE Devicelist(id integer PRIMARY KEY, IPaddress text,\
                            username text, password text, Devicetype text)")
        con.commit()
    except db3.OperationalError as e:
        print('exist')        
    except db3.Error as e:
        print (e)
con = dbconnection.sql_connection(db3)

sql_table(con)
