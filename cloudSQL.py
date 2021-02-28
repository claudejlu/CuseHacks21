import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'root',
    'password': 'pizzapopper123456',
    'host': '35.247.45.15',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca.pem',
    'ssl_cert': 'ssl/client-cert.pem',
    'ssl_key': 'ssl/client-key.pem'
}

class cloudSQL():
    
    def createDatabase(self, name):
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor()
        cursor.execute('CREATE DATABASE ' + name)
        cnxn.close()
    
    def createTable(self, databaseName, query):
        config['database'] = databaseName 
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor()

        cursor.execute(query)
        cnxn.commit()
        cnxn.close()

    # data = (username, room)
    def addData(self, databaseName, data):
        config['database'] = databaseName 
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor()

        query = "INSERT INTO roomsTable (username, room) VALUES "  + data +  ";"
        cursor.execute(query)
        cnxn.commit()  # and commit changes
        cnxn.close()

    def listData(self, databaseName, room):
        config['database'] = databaseName 
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor()

        query = "SELECT * FROM roomsTable WHERE room=" + room +  ";"
        cursor.execute(query)
        out = cursor.fetchAll()
        cnxn.close()
        return out



# x = cloudSQL()
# x.createTable("testdb", "CREATE TABLE roomsTable ("

#                "username VARCHAR(255),"

#                "room VARCHAR(255),"

#                "primary key (username, room) )"
# )
    