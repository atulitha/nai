def sql_connection(db3):
    try:
        con = db3.connect('mydatabase.db')
        print ('connected to db')
        return con
    except db3.Error as Error:
        print (Error)
        return(Error)
 
