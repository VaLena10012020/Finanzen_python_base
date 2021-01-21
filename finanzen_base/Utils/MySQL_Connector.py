import mysql.connector

class MySQL_Connector():
    def __init__(self, database:str):
        self.mydb = mysql.connector.connect(
            host="localhost",
            port='3307',
            user="root",
            password="root",
            database=database
        )

    def get_SQL(self, SQL_statement: str):
        curs = con.mydb.cursor()
        curs.execute(SQL_statement)
        sql_return = curs.fetchall()
        curs.close()
        return sql_return

    def insert_SQL(self, SQL_statement: str):
        curs = con.mydb.cursor()
        curs.execute(SQL_statement)
        curs.close()



con = MySQL_Connector(database="Finanzen")
print(type(con.get_SQL("SELECT DISTINCT date FROM LOHN")))
