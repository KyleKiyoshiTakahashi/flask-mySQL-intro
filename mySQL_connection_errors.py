
import pymysql.cursors

class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(host = 'localhost: 
                                    user = 'root', 
                                    password = 'root' 
                                    db = db,
                                    charset = utf8mb4,
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = true
        
        self.connection = connection
  
    def query_db(self, query):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
     
                executable = cursor.execute(query, data)
                if query.lower().find("insert") > 0:
                   
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") > 0:
                    
                    result = cursor.fetchall()
                    return result;
                else
                   
                    self.connection.commit()
            except Exception as e:
               
                print("Something went wrong", e)
                return False
            finally:
                
                self.connection.close() 

def connectToMySQL(db):
    return MySQL(db)


# line 6 is missing and ending '' and a comma. get rid of the colin.
# line 10 needs ''
# line 12 needs a closing )

# line 16, needs data=None
# line 22, should be >=
# line 27 shoudl be >=
# line 31 needs : after the else
# 