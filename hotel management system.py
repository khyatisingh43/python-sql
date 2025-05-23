print("**********************************************************************************************")
print("*_*                                         HOTEL MANAGEMENT SYSTEM                                                                 ^_^")
print("**********************************************************************************************")
roomrent=0
restaurentbill=0
gamingbill=0
laundrybill=0
shoppingbill=0
totalAmount=0
cid=""
import mysql.connector 
mydb=mysql.connector.connect(host="localhost",user="root",password="CLASS12khyati@@")
cursor=mydb.cursor()
cursor=myConnection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS HMS")
cursor.execute("COMMIT")
cursor.close()
def MYSQLconnection () :
    myConnection=mysql.connector.connect(host="localhost",user="root",passwd="CLASS12khyati@@", database="HMS" , auth_plugin='mysql_native_password' )
    if myConnection:
        return myConnection
    else:
       print("\nERROR ESTABLISHING MYSQL CONNECTION !")
    myConnection.close()


def customerDetails():
    global cid
    if mydb:
        cursor=mydb.cursor (createTable= """CREATE TABLE IF NOT EXISTS C_DETAILS(CID VARCHAR(20),C_NAME VARCHAR(30),C_ADDRESS VARCHAR(30),C_AGE VARCHAR(30),
C_COUNTRY VARCHAR(30) ,P_NO VARCHAR(30),C_EMAIL VARCHAR(30))"""
        cursor.execute(createTable)
                            cid = input("Enter Customer Identification Number : ")
                            name = input("Enter Customer Name : ")
                            address=input("enter customers address")
                            age= input("Enter Customer Age : ")
                            nationality = input("Enter Customer Country : ")
                            phoneno= input("Enter Customer Contact Number : ")
                            email = input("Enter Customer Email : ")
                            sql="INSERT INTO C_Details VALUES(%s,%s,%s,%s,%s,%s,%s)" values=(cid,name,address,age,nationality,phoneno,email)
                            cursor.execute(sql,values)
                            cursor.execute ("COMMIT")
                            print("customer details entered succesfully")
            cursor.close()
                            
