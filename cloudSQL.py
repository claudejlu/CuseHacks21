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

    # data = ('username', 'room')
    def addData(self, databaseName, name, room):
        config['database'] = databaseName 
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor()

        query = "INSERT INTO roomsTable VALUES (%s, %s);"
        cursor.execute(query, (name, room))
        cnxn.commit()
        cnxn.close()

    def listData(self, databaseName, room):
        config['database'] = databaseName 
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor()

        query = "SELECT * FROM roomsTable WHERE room = %s;"
        # query = "SELECT * FROM roomsTable;"

        cursor.execute(query, (room,))
        # cursor.execute(query)
        out = cursor.fetchall()
        cnxn.close()
        return out
    
    def removeData(self, databaseName, room, name):
        config['database'] = databaseName 
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor()

        query = "DELETE FROM roomsTable WHERE room = %s AND username = %s;"
        cursor.execute(query, (room, name))
        cnxn.commit()
        cnxn.close()



# x = cloudSQL()
# x.addData('testdb', 'Fred', '123')
# x.removeData('testdb', '123', 'Fred')
# output = x.listData('testdb', '123')
# print(output)


# config['database'] = 'testdb' 
# cnxn = mysql.connector.connect(**config)
# cursor = cnxn.cursor()

# query = "SELECT * FROM roomsTable;"
# cursor.execute(query)
# out = cursor.fetchall()
# print(out)
# cnxn.close()



# x = cloudSQL()
# x.createTable("testdb", "CREATE TABLE roomsTable ("

#                "username VARCHAR(255),"

#                "room VARCHAR(255),"

#                "primary key (username, room) )"
# )
    