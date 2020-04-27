import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="rail");
mycursor=mydb.cursor()

print("Trains Available")
query = "select tname,tnum from traindetail"
mycursor.execute(query)
train = mycursor.fetchall()
for x in train:
    print(x)