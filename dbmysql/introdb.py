import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    #database="adso"
)
print(type(db))
cursor=db.cursor()
cursor.execute("SHOW DATABASES")
print(cursor)
for dbs in cursor:
    print(dbs)

#bsucar ubna base de datos 