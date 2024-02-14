import mysql.connector as con
import os
import datetime
import re
import smtplib
import random
path = con.connect(host = 'localhost', username = 'root', password = '@Hrishiadi200136', port = '3306')
db = path.cursor()
'''db.execute("CREATE DATABASE STOREMANAGERPY")'''
db.execute("USE STOREMANAGERPY;")
'''
db.execute("CREATE TABLE Custdata (S_No INT NOT NULL AUTO_INCREMENT,CustEmail VARCHAR(50) Not null,CustUser VARCHAR(50) NOT NULL,CustPass VARCHAR(50) NOT null,Custname VARCHAR(50) NOT NULL,CustAge int NOT NULL,CustCountryOR VARCHAR(50) NOT NULL,CustCityOR VARCHAR(50) NOT NULL,CustDateofentry DATE NOT NULL,CustTimeofentry TIME Not Null,CustDateOB date Not null,CustPhoneno VARCHAR(50) NOT NULL,CustCardcolour varchar(50), CustPoints int, CustGender varchar(50),PRIMARY KEY(S_No));")
db.execute("CREATE TABLE Empdata (S_No INT NOT NULL AUTO_INCREMENT,EmpEmail VARCHAR(50) Not null,EmpUser VARCHAR(50) NOT NULL,EmpPass VARCHAR(50) NOT null,Empname VARCHAR(50) NOT NULL,EmpAge int NOT NULL,EmpCountryOR VARCHAR(50) NOT NULL,EmpCityOR VARCHAR(50) NOT NULL,EmpDateofentry DATE NOT NULL,EmpTimeofentry TIME Not Null,EmpDateOB date Not null,EmpPhoneno VARCHAR(50) NOT NULL,EmpCardcolour varchar(50), EmpPoints int, EmpGender varchar(50),EmpStore Varchar(50),PRIMARY KEY(S_No));")
db.execute("CREATE TABLE Storedata (S_No INT NOT NULL AUTO_INCREMENT,StoreEmail VARCHAR(50) Not null,StoreName VARCHAR(50),StoreCountry VARCHAR(50),StoreCity Varchar(50), StoreUser VARCHAR(50) NOT NULL,StorePass VARCHAR(50) NOT null,DOEstablish Date,StoreDateofentry DATE NOT NULL,StoreTimeofentry TIME Not Null,StorePhoneno VARCHAR(50) NOT NULL,PRIMARY KEY(S_No));")
db.execute("CREATE TABLE Productsdata (S_No INT NOT NULL AUTO_INCREMENT, ProdName VARCHAR(50), ProdCompany VARCHAR(50), ProdCode VARCHAR(50), ProdCategory VARCHAR(50), ProdPrice_inr INT,StoreName VARCHAR(50), PRIMARY KEY(S_No));")
db.execute("Create table Logindata (S_No INT NOT NULL AUTO_INCREMENT, AccountSpecifications Varchar(50),User VARCHAR(50) NOT NULL,Pass VARCHAR(50) NOT null,Email VARCHAR(50) Not null,PRIMARY KEY(S_No));")
db.execute("CREATE TABLE Cart (S_No INT NOT NULL AUTO_INCREMENT, ProdName VARCHAR(50), ProdCompany VARCHAR(50), ProdCode VARCHAR(50), ProdCategory VARCHAR(50), ProdPrice_inr INT, AccountSpecifications Varchar(50),User VARCHAR(50) NOT NULL,Pass VARCHAR(50) NOT null,Email VARCHAR(50) Not null, PRIMARY KEY(S_No));")
db.execute("CREATE TABLE task (S_No INT NOT NULL AUTO_INCREMENT, Task varchar(7500), Status varchar(50),StoreName Varchar(50), Empname varchar(50), PRIMARY KEY(S_No));")
'''
print("Welcome To THE STORE MANAGER")
print('*' * 157)
intezer=1
a=10000
Accspecs=''
while a ==10000  :
    ans_two=0
    print("""
SELECT
_______________
| 1 | Sign In |
| 2 | Log In  |
| 3 | Exit    |
~~~~~~~~~~~~~~~
""")
    ans_one=int(input("==>"))
    if type(ans_one) == type(intezer):
        print()
    else:
        print("Invalid Entry")
        break
    if ans_one >2:
        a=1
        break
    while ans_one ==1:
        print("""
SELECT
_______________________________
| 1 | Customer Registration   |
| 2 | Employee Registration   |
| 3 | Store Registration      |
| 4 | Back To Main Menu       |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
        if type(ans_one) == type(intezer):
            print()
        else:
            print("Invalid Entry")
            break
        ans_two = int(input("==>"))
        if ans_two > 3 :
            
            break
        db.execute("SELECT User,Email from Logindata")
        logindata=db.fetchall()
        while ans_two == 1:
            Username=''
            while Username == '':
                Username=str(input("Enter Username ==>"))
                for row in logindata:
                    if row[0] == Username :
                        print("""Username Is already taken.
Please Re-enter your Username""")
                        Username = ''
                    elif row[0] != Username:
                        print('',end='')
            Password_a=' '
            Password_b=''
            while Password_a != Password_b:
                Password_a=str(input("Enter Password ==>"))
                Password_b=str(input("Re-enter Password ==>"))
            Name=str(input("Enter Your Name ==>"))
            Name.upper()
            Email=""
            while Email == "":
                EmailDomain= str(input("Enter Domain of Your Gmail ==>"))
                EmailDomain.strip()
                EmailDomain.lower()
                EmailDomain.strip()
                Email=EmailDomain+'@gmail.com'
                for row in logindata:
                    if row[1] == Email :
                        print("""Email Is already Used by Another User.
Please Re-enter your Username""")
                        Username == ''
                    elif row[0] != Username:
                        print('',end='')
            Age=int(input("Enter Your Age ==>"))
            CountryOR=str(input("Please Enter Your Country of Residence"))
            CityOR=str(input("Please Enter Your City of Residence"))
            DateTimeofentry=datetime.datetime.now()
            x=str(DateTimeofentry).split(' ')
            Dateofentry=x[0]
            Timeofentry=x[1]
            ans=1
            while ans == 1:
                try:
                    day=int(input("Day of Birth:"))
                    month=int(input("Month of Birth(In Numbers):"))
                    year=int(input("Year of Birth:"))
                    dob=datetime.date(year,month,day)
                    ans = 2
                except ValueError :
                    print("Invalid Entry")
            Phoneno=str(input("Enter Your Phone Number"))
            print("""Please Select
_______________________
| 1 | 'Gold' Card     |
| 2 | 'Silver' Card   |
| 3 | 'Platinum' Card |
~~~~~~~~~~~~~~~~~~~~~~~
""")
            ans_a=int(input("==>"))
            if ans_a == 1:
                Cardcolour='GOLD'
            elif ans_a == 2:
                Cardcolour='SILVER'
            elif ans_a == 3:
                Cardcolour='PLATINUM'
            points=0
            Gender=str(input("Enter Your Gender (Male : M,Female : F, etc.)==>"))
            Accspecs='CUSTOMER'
            db.execute("INSERT INTO Custdata (CustEmail, CustUser, CustPass, Custname, CustAge,CustCountryOR,CustCityOR,CustDateofentry,CustTimeofentry,CustDateOB,CustPhoneno,CustCardcolour,CustPoints,CustGender) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');". format(Email,Username,Password_a,Name,Age,CountryOR,CityOR,Dateofentry,Timeofentry,dob,Phoneno,Cardcolour,points,Gender))
            path.commit()
            db.execute("INSERT INTO Logindata (AccountSpecifications, User,Pass,Email) VALUES ('{}', '{}', '{}', '{}');". format(Accspecs,Username,Password_a,Email))
            path.commit()
            print("Account Registration Sucessful")
            print("Thankyou For Choosing STORE MANAGER")
            ans_two == 4
            Accspecs=''
            break
        while ans_two == 2:
            Username=''
            while Username == '':
                Username=str(input("Enter Username ==>"))
                for row in logindata:
                    if row[0] == Username :
                        print("""Username Is already taken.
Please Re-enter your Username""")
                        Username == ''
                    elif row[0] != Username:
                        print("",end='')
            Password_a=' '
            Password_b=''
            while Password_a != Password_b:
                Password_a=str(input("Enter Password ==>"))
                Password_b=str(input("Re-enter Password ==>"))
            Name=str(input("Enter Your Name ==>"))
            Name.upper()
            Email=""
            while Email == "":
                EmailDomain= str(input("Enter Domain of Your Gmail ==>"))
                EmailDomain.strip()
                EmailDomain.lower()
                EmailDomain.strip()
                Email=EmailDomain+'@gmail.com'
                for row in logindata:
                    if row[1] == Email :
                        print("""Email Is already Used by Another User.
Please Re-enter your Username""")
                        Username == ''
                    elif row[0] != Username:
                        print('',end='')
            Age=int(input("Enter Your Age ==>"))
            CountryOR=str(input("Please Enter Your Country of Residence"))
            CityOR=str(input("Please Enter Your City of Residence"))
            DateTimeofentry=datetime.datetime.now()
            x=str(DateTimeofentry).split(' ')
            Dateofentry=x[0]
            Timeofentry=x[1]
            ans=1
            while ans == 1:
                try:
                    day=int(input("Day of Birth:"))
                    month=int(input("Month of Birth(In Numbers):"))
                    year=int(input("Year of Birth:"))
                    dob=datetime.date(year,month,day)
                    ans = 2
                except ValueError :
                    print("Invalid Entry")
            Phoneno=str(input("Enter Your Phone Number"))
            print("""Please Select
_______________________
| 1 | 'Gold' Card     |
| 2 | 'Silver' Card   |
| 3 | 'Platinum' Card |
~~~~~~~~~~~~~~~~~~~~~~~
""")
            ans_a=int(input("==>"))
            if ans_a == 1:
                Cardcolour='GOLD'
            elif ans_a == 2:
                Cardcolour='SILVER'
            elif ans_a == 3:
                Cardcolour='PLATINUM'
            points=0
            Gender=str(input("Enter Your Gender (Male : M,Female : F, etc.)==>"))
            Accspecs='EMPLOYEE'
            EmpStore=''
            while EmpStore == '':
                db.execute("SELECT MAX(LENGTH(StoreName)), MAX(LENGTH(S_no)) from Storedata;")
                length=db.fetchone()
                db.execute("SELECT StoreName, S_no from Storedata;")
                Sname=db.fetchall()
                for x in Sname :
                    psname="{:<3} {:<"+str(length[1]+2)+"} {:<3} {:<"+str(length[0]+2)+"} {:<3}"
                    print(psname.format('|',str(x[1]),'|',x[0],'|'))
                EmpStore=int(input("Select the Serial Number of the store you  work for ==>"))
                db.execute("SELECT StoreName from Storedata where S_No = "+str(EmpStore)+";")
                Sname=db.fetchone()
                EmpStore=Sname[0]
            db.execute("INSERT INTO Empdata (EmpEmail, EmpUser, EmpPass, Empname, EmpAge,EmpCountryOR,EmpCityOR,EmpDateofentry,EmpTimeofentry,EmpDateOB,EmpPhoneno,EmpCardcolour,EmpPoints,EmpGender,EmpStore) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(Email,Username,Password_a,Name,Age,CountryOR,CityOR,Dateofentry,Timeofentry,dob,Phoneno,Cardcolour,points,Gender,EmpStore))
            path.commit()
            db.execute("INSERT INTO Logindata (AccountSpecifications, User,Pass,Email) VALUES ('{}', '{}', '{}', '{}');".format(Accspecs,Username,Password_a,Email))
            path.commit()
            print("Account Registration Sucessful")
            print("Thankyou For Choosing STORE MANAGER")
            ans_two == 4
            Accspecs=''
            break
        while  ans_two == 3:
            Username=''
            while Username == '':
                Username=str(input("Enter Username ==>"))
                for row in logindata:
                    if row[0] == Username :
                        print("""Username Is already taken.
Please Re-enter your Username""")
                        Username == ''
                    elif row[0] != Username:
                        print('',end='')
            Password_a=' '
            Password_b=''
            while Password_a != Password_b :
                Password_a=str(input("Enter Password ==>"))
                Password_b=str(input("Re-enter Password ==>"))
            Name=str(input("Enter The Name of Your Store==>")).upper()
            Email=""
            while Email == "":
                EmailDomain= str(input("Enter Domain of Your Gmail ==>")).lower()
                EmailDomain.strip()
                Email=EmailDomain+'@gmail.com'
                for row in logindata:
                    if row[1] == Email :
                        print("""Email Is already Used by Another User.
Please Re-enter your Username""")
                        Username == ''
                    elif row[0] != Username:
                        print('',end='')
            CountryOR=str(input("Please Enter Your Country of Residence"))
            CityOR=str(input("Please Enter Your City of Residence"))
            DateTimeofentry=datetime.datetime.now()
            x=str(DateTimeofentry).split(' ')
            Dateofentry=x[0]
            Timeofentry=x[1]
            ans=1
            while ans == 1:
                try:
                    day=int(input("Day of Establishment:"))
                    month=int(input("Month of Establishment(In Numbers):"))
                    year=int(input("Year of Establishment:"))
                    dob=datetime.date(year,month,day)
                    ans = 2
                except ValueError :
                    print("Invalid Entry")
            Phoneno=str(input("Enter Your Phone Number"))
            Accspecs='STORE'
            db.execute("INSERT INTO Storedata (StoreEmail, StoreUser, StorePass, Storename, StoreCountry,StoreCity,StoreDateofentry,StoreTimeofentry,DOEstablish,StorePhoneno) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(Email,Username,Password_a,Name,CountryOR,CityOR,Dateofentry,Timeofentry,dob,Phoneno))
            path.commit()
            db.execute("INSERT INTO Logindata (AccountSpecifications, User,Pass,Email) VALUES ('{}', '{}', '{}', '{}');".format(Accspecs,Username,Password_a,Email))
            path.commit()
            print("Account Registration Sucessful")
            print("Thankyou For Choosing STORE MANAGER")
            ans_two == 4
            Accspecs=''
            break
        break
    while ans_two == 4 :
        ans_one = 3
        break
    while ans_one ==1 or ans_one ==2:
        db.execute("SELECT User,Pass,AccountSpecifications,Email from Logindata")
        logindata=db.fetchall()
        print("""Select to Log In Using
__________________________
| 1 | Email              |
| 2 | Username           |
| 3 | Back To Main Menu  |
~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
        ans_log = int(input("==>"))
        while ans_log >= 3:
            break
        while ans_log == 2:
            gmail=''
            Username=''
            Row1=()
            while Username == '':
                Username=str(input("Enter Username ==>"))
                for row in logindata:
                    while row[0] == Username :
                        print("Username Valid")
                        Row1=row
                        break
                if Row1==():
                    Username=''
            Password = ''
            while Password == '':
                Password=str(input("Enter Password ==>"))
                if Row1[1] == Password :
                    print("Password Valid")
                elif Row1[1] != Password:
                    print("Password Invalid")
                    Password = ''
            if Row1[1] == Password :
                Accspecs=Row1[2]
                gmail = Row1[3]
                Password = Row1[1]
                Username=Row1[0]
                a=1
                break
            break
        while ans_log == 1:
            username=''
            gmail=''
            Row1=()
            while gmail == '':
                gmail=str(input("Enter Email ID==>"))
                for row in logindata:
                    while row[3] == gmail :
                        print("Email Valid")
                        Row1=row
                        break
                if Row1== () :
                        gmail = ''
            Password = ''
            while Password == '':
                Password=str(input("Enter Password ==>"))
                if Row1[1] == Password :
                    print("Password Valid")
                elif Row1[1] != Password:
                    print("Password Invalid")
                    Password = ''
            if Row1[1] == Password :
                Accspecs=Row1[2]
                gmail = Row1[3]
                Password = Row1[1]
                Username=Row1[0]
                a=1
                break
            break
        break
    continue
a=1000
while a==1000:
    if Accspecs == '':
        a=1 
    if Accspecs == 'CUSTOMER':
        print(""" SELECT
______________________
| 1 | Veiw Products  |
| 2 | Veiw Cart      |
| 3 | Veiw Profile   |
| 4 | Log Out        |
~~~~~~~~~~~~~~~~~~~~~~
""")
        ans_cust=int(input("==>"))
        if type(ans_cust) == type(intezer):
            print()
        else:
            print("Invalid Entry")
            break
        while ans_cust==4:
            a=1
            break
        while ans_cust != 4:
            while ans_cust == 1:
                db.execute("Select MAX(Length(S_No)),MAX(LENGTH(ProdName)),MAX(LENGTH(ProdCompany)),MAX(LENGTH(ProdCode)),MAX(LENGTH(ProdCategory)),MAX(LENGTH(ProdPrice_inr)),MAX(LENGTH(StoreName)) from Productsdata;")
                numlist=db.fetchone()
                db.execute("Select * from Productsdata; ")
                Products=db.fetchall()
                print("_"*157)
                for row in Products:
                    Pprod="{:<3} {:<"+str(numlist[0]+2)+"} {:<3} {:<"+str(numlist[1]+2)+"} {:<3} {:<"+str(numlist[2]+2)+"} {:<3} {:<"+str(numlist[3]+2)+"} {:<3} {:<"+str(numlist[4]+2)+"} {:<3} {:<"+str(numlist[5]+2)+"} {:<3} {:<"+str(numlist[6]+2)+"} {:<3}"
                    print(Pprod.format("|",str(row[0]),"|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",row[5],"|",str(row[6]),"|"))
                print("~"*157)
                print("""Select
____________________
| 1 | Add To Cart  |
| 2 | Exit         |
~~~~~~~~~~~~~~~~~~~~
""")
                ans_cust2= int(input("==>"))
                while ans_cust2 != 2:
                    while ans_cust2 == 1:
                        PCode=str(input("Enter the  Product Code of the Product you want to add to your Cart ==>"))
                        db.execute("Select ProdName, ProdCompany,ProdCode,ProdCategory,ProdPrice_inr from Productsdata where ProdCode = '"+PCode+"';")
                        Products=db.fetchone()
                        db.execute("INSERT INTO Cart (ProdName,ProdCompany,ProdCode,ProdCategory,ProdPrice_inr,AccountSpecifications, User, Pass, Email) VALUES ('{}', '{}', '{}', '{}','{}','{}','{}','{}','{}');".format(Products[0],Products[1],Products[2],Products[3],Products[4],Accspecs,Username,Password,gmail))
                        path.commit()
                        ans_cust2=2
                        break
                if ans_cust2 == 2:
                    print()
                    break
                ans_cust=4
                break
            while ans_cust==2:
                db.execute("Select LENGTH(MAX(S_No)),MAX(LENGTH(ProdName)),MAX(LENGTH(ProdCompany)),MAX(LENGTH(ProdCode)),MAX(LENGTH(ProdCategory)),MAX(LENGTH(ProdPrice_inr)) from Cart where (Email = '"+ gmail + "' or User = '"+ Username +"') and Pass = '"+ Password +"';")
                numlist=db.fetchone()
                db.execute("Select * from Cart where (Email = '"+ gmail + "' or User = '"+ Username +"') and Pass = '"+ Password +"';")
                CartProds=db.fetchall()
                print("_"*157)
                print
                for row in CartProds:
                    Pcart="{:<3} {:<"+str(numlist[0]+2)+"} {:<3} {:<"+str(numlist[1]+2)+"} {:<3} {:<"+str(numlist[2]+2)+"} {:<3} {:<"+str(numlist[3]+2)+"} {:<3} {:<"+str(numlist[4]+2)+"} {:<3} {:<"+str(numlist[5]+2)+"} {:<3}"
                    print(Pcart.format("|",str(row[0]),"|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",row[5],"|"))
                print("~"*157)
                print("""Select
_____________________________
| 1 | Delete a Product      |
| 2 | Purchase the Products |
| 3 | Exit                  |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
                ans_cart=int(input("==>"))
                while ans_cart != 3:
                    while ans_cart==1:
                        DelprodCode=input("Enter the Product Code of the Product you want to Delete")
                        x=[]
                        for row in CartProds:
                            if row[3] == DelprodCode:
                                x.append(row)
                                db.execute("DELETE from Cart where (Email = '"+ gmail + "' or User = '"+ Username +"') and ProdCode = '"+row[3]+"';")
                                path.commit()
                                ans_cart = 3
                        if x == [] :
                            print("Invalid Entry")
                            ans_cart = 3
                        break
                    while ans_cart == 2:
                        db.execute("SELECT SUM(ProdPrice_inr) from Cart where (Email = '"+ gmail + "' or User = '"+ Username +"') and Pass = '"+ Password +"';")
                        totalcost=db.fetchone()
                        print("The total cost of the products: ",totalcost[0])
                        print("""
________ _______
| 1 | Confirm |
| 2 | Cancel  |
~~~~~~~~~~~~~~~
""")
                        ans_purchase=int(input("==>"))
                        while ans_purchase < 2:
                            print("Thankyou For The Purchase")
                            ans_purchase = 3
                            break
                        ans_cart = 3
                        ans_cust=3
                        break
                    ans_cust=4
                    break
                break
            while ans_cust == 3:
                db.execute("SELECT * from Custdata where ( CustEmail = '"+ gmail + "' or CustUser = '"+ Username +"') and CustPass = '"+ Password +"';")
                custdetails=db.fetchone()
                print("_"*157)
                print("| Name : ", custdetails[4])
                print("| Username : ", custdetails[2])
                print("| Email :" ,custdetails[1])
                print("| Age : ", custdetails[5])
                print("| Gender : ", custdetails[14])
                print("| Country Of Residence : ", custdetails[6])
                print("| City Of Residence : ", custdetails[7])
                print("| Registration Date : ", custdetails[8])
                print("| Regitration Time : ", custdetails[9])
                print("| Date Of Birth : ", custdetails[10])
                print("| Phone Number : ", custdetails[11])
                print("| Card Colour : ", custdetails[12])
                print("| Points : ", custdetails[13])
                print("~"*157)
                print()
                print()
                print("|SELECT|")
                print("""
______________________
| 1 | Update Profile |
| 2 | Exit           |
~~~~~~~~~~~~~~~~~~~~~~
""")
                anscustprofile=int(input("==>"))
                while anscustprofile == 1:
                    print("""|SELECT to Update|               
____________________________                     
| 1 | Email                | 
| 2 | Age                  |
| 3 | Country Of Residence |   
| 4 | City Of Residence    |
| 5 | Phone Number         |
| 6 | Password             |
| 7 | Exit                 |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
                    ansUprofileEdit=int(input("==>"))
                    while ansUprofileEdit < 7:
                        while ansUprofileEdit == 1:
                            newmail=input("Enter New Email : ")
                            db.execute("Update Custdata SET CustEmail = '"+newmail+"' where ( CustEmail = '"+ gmail + "' or CustUser = '"+ Username +"') and CustPass = '"+ Password +"';")
                            path.commit()
                            db.execute("Update Logindata Email = '"+newmail+"' where ( Email = '"+ gmail + "' or User = '"+ Username +"') and Pass = '"+ Password +"';")
                            path.commit()
                            ansUprofileEdit = 7
                            break
                        while ansUprofileEdit == 2:
                            newage=input("Enter Age: ")
                            db.execute("Update Custdata SET  CustAge = "+newage+" where ( CustEmail = '"+ gmail + "' or CustUser = '"+ Username +"') and CustPass = '"+ Password +"';")
                            path.commit()
                            ansUprofileEdit = 7
                            break
                        while ansUprofileEdit == 3:
                            newCountry=input("Enter Country: ")
                            db.execute("Update Custdata SET  CustCountryOR = '"+newCountry+"' where ( CustEmail = '"+ gmail + "' or CustUser = '"+ Username +"') and CustPass = '"+ Password +"';")
                            path.commit()
                            ansUprofileEdit = 7
                            break
                        while ansUprofileEdit == 4:
                            newcity=input("Enter City: ")
                            db.execute("Update Custdata SET  CustCityOR = '"+newcity+"' where ( CustEmail = '"+ gmail + "' or CustUser = '"+ Username +"') and CustPass = '"+ Password +"';")
                            path.commit()
                            ansUprofileEdit = 7
                            break
                        while ansUprofileEdit == 5:
                            newPhoneno=input("Enter Phone Number: ")
                            db.execute("Update Custdata SET  CustPhoneno = '"+newPhoneno+"' where ( CustEmail = '"+ gmail + "' or CustUser = '"+ Username +"') and CustPass = '"+ Password +"';")
                            path.commit()
                            ansUprofileEdit = 7
                            break
                        while ansUprofileEdit == 6:
                            newPass=input("Enter New Password")
                            db.execute("Update Custdata SET  CustPass = '"+newPass+"' where ( CustEmail = '"+ gmail + "' or CustUser = '"+ Username +"') and CustPass = '"+ Password +"';")
                            path.commit()
                            db.execute("Update Logindata Pass = '"+newpass+"' where ( Email = '"+ gmail + "' or User = '"+ Username +"') and Pass = '"+ Password +"';")
                            path.commit()
                            ansUprofileEdit = 7
                            break
                        break
                    break
                ans_cust=4
                break
            break
        continue
    if Accspecs == 'EMPLOYEE':
        print(""" SELECT
______________________
| 1 | Veiw Products  |
| 2 | Veiw Cart      |
| 3 | Veiw Profile   |
| 4 | Veiw Tasks     |
| 5 | Log Out        |
~~~~~~~~~~~~~~~~~~~~~~
""")
        ans_emp =int(input("==>"))
        if type(ans_emp) == type(intezer):
            print()
        else:
            print("Invalid Entry")
            break
        while ans_emp == 5:
            a=1
            break
        while ans_emp != 5:
            while ans_emp == 1:
                db.execute("Select MAX(Length(S_No)),MAX(LENGTH(ProdName)),MAX(LENGTH(ProdCompany)),MAX(LENGTH(ProdCode)),MAX(LENGTH(ProdCategory)),MAX(LENGTH(ProdPrice_inr)),MAX(LENGTH(StoreName)) from Productsdata;")
                numlist=db.fetchone()
                db.execute("Select * from Productsdata; ")
                Products=db.fetchall()
                print("_"*157)
                for row in Products:
                    Pprod="{:<3} {:<"+str(numlist[0]+2)+"} {:<3} {:<"+str(numlist[1]+2)+"} {:<3} {:<"+str(numlist[2]+2)+"} {:<3} {:<"+str(numlist[3]+2)+"} {:<3} {:<"+str(numlist[4]+2)+"} {:<3} {:<"+str(numlist[5]+2)+"} {:<3} {:<"+str(numlist[6]+2)+"} {:<3}"
                    print(Pprod.format("|",str(row[0]),"|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",row[5],"|",str(row[6]),"|"))
                print("~"*157)
                print("""Select
___________________
| 1 | Add To Cart |
| 2 | Exit        |
~~~~~~~~~~~~~~~~~~~
""")
                ans_emp2= int(input("==>"))
                while ans_emp2 != 2:
                    while ans_emp2 == 1:
                        PCode=str(input("Enter the  Product Code of the Product you want to add to your Cart ==>"))
                        db.execute("Select ProdName, ProdCompany,ProdCode,ProdCategory,ProdPrice_inr from Productsdata where ProdCode = '"+PCode+"';")
                        Products=db.fetchone()
                        db.execute("INSERT INTO Cart (ProdName,ProdCompany,ProdCode,ProdCategory,ProdPrice_inr,AccountSpecifications, User, Pass, Email) VALUES ('{}', '{}', '{}', '{}','{}','{}','{}','{}','{}');".format(Products[0],Products[1],Products[2],Products[3],Products[4],Accspecs,Username,Password,gmail))
                        path.commit()
                        ans_emp2 = 2
                        break
                    if ans_emp2 >= 2:
                        print()
                        break
                    ans_emp2=2
                    break
                ans_emp=5
                break
            while ans_emp==2:
                db.execute("Select LENGTH(MAX(S_No)),MAX(LENGTH(ProdName)),MAX(LENGTH(ProdCompany)),MAX(LENGTH(ProdCode)),MAX(LENGTH(ProdCategory)),MAX(LENGTH(ProdPrice_inr)) from Cart where (Email = '"+ gmail + "' or User = '"+ Username +"') and Pass = '"+ Password +"';")
                numlist=db.fetchone()
                db.execute("Select * from Cart where (Email = '"+ gmail + "' or User = '"+ Username +"') and Pass = '"+ Password +"';")
                CartProds=db.fetchall()
                print("_"*157)
                print
                for row in CartProds:
                    Pcart="{:<3} {:<"+str(numlist[0]+2)+"} {:<3} {:<"+str(numlist[1]+2)+"} {:<3} {:<"+str(numlist[2]+2)+"} {:<3} {:<"+str(numlist[3]+2)+"} {:<3} {:<"+str(numlist[4]+2)+"} {:<3} {:<"+str(numlist[5]+2)+"} {:<3}"
                    print(Pcart.format("|",str(row[0]),"|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",row[5],"|"))
                print("~"*157)
                print("""Select
_____________________________
| 1 | Delete a Product      |
| 2 | Purchase the Products |
| 3 | Exit                  |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
                ans_cart=int(input("==>"))
                while ans_cart != 3:
                    while ans_cart==1:
                        DelprodCode=input("Enter the Product Code of the Product you want to Delete")
                        x=[]
                        for row in CartProds:
                            if row[3] == DelprodCode:
                                x.append(row)
                                db.execute("DELETE from Cart where (Email = '"+ gmail + "' or User = '"+ Username +"') and ProdCode = '"+row[3]+"';")
                                path.commit()
                                ans_cart = 3
                        if x == [] :
                            print("Invalid Entry")
                            ans_cart = 3
                        break
                    while ans_cart == 2:
                        db.execute("SELECT SUM(ProdPrice_inr) from Cart where (Email = '"+ gmail + "' or User = '"+ Username +"') and Pass = '"+ Password +"';")
                        totalcost=db.fetchone()
                        print("The total cost of the products: ",totalcost[0])
                        print("""
_______________
| 1 | Confirm |
| 2 | Cancel  |
~~~~~~~~~~~~~~~
""")
                        ans_purchase=int(input("==>"))
                        while ans_purchase < 2:
                            print("Thankyou For The Purchase")
                            ans_cart = 3
                            break
                        ans_cart = 3
                        ans_cust=3
                ans_emp = 5
                break
            while ans_emp == 3:
                db.execute("SELECT * from Empdata where ( EmpEmail = '"+ gmail + "' or EmpUser = '"+ Username +"') and EmpPass = '"+ Password +"';")
                empdetails=db.fetchone()
                print("_"*157)
                print("| Name : ", empdetails[4] )
                print("| Username : ", empdetails[2] )
                print("| Email : " ,empdetails[1] )
                print("| Age : ", empdetails[5] )
                print("| Gender : ", empdetails[14] )
                print("| Country Of Residence : ", empdetails[6] )
                print("| City Of Residence : ", empdetails[7] )
                print("| Registration Date : ", empdetails[8] )
                print("| Regitration Time : ", empdetails[9] )
                print("| Date Of Birth : ", empdetails[10] )
                print("| Phone Number : ", empdetails[11] )
                print("| Card Colour : ", empdetails[12] )
                print("| Points : ", empdetails[13] )
                print("| Store : ", empdetails[15] )
                print("~"*157)
                print()
                print()
                print("|SELECT|")
                print("""
_______________________
| 1 | Update Profile  |
| 2 | Exit            |
~~~~~~~~~~~~~~~~~~~~~~~
""")
                ansempprofile=int(input("==>"))
                while ansempprofile == 1:
                    print("""|SELECT to Update|
_____________________________                     
| 1 | Email                 | 
| 2 | Age                   |
| 3 | Country Of Residence  |
| 4 | City Of Residence     |
| 5 | Phone Number          |
| 6 | Password              |
| 7 | Exit                  |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
                    ansEprofileEdit=int(input("==>"))
                    while ansEprofileEdit < 7 :
                        while ansEprofileEdit == 1:
                            newmail=input("Enter New Email : ")
                            db.execute("Update Empdata SET EmpEmail = '"+newmail+"' where ( EmpEmail = '"+ gmail + "' or EmpUser = '"+ Username +"') and EmpPass = '"+ Password +"';")
                            path.commit()
                            db.execute("Update Logindata SET EmpEmail = '"+newmail+"' where ( Email = '"+ gmail + "' or User = '"+ Username +"') and Pass = '"+ Password +"';")
                            path.commit()
                            ansEprofileEdit = 7
                            break
                        while ansEprofileEdit == 2:
                            newage=input("Enter Age: ")
                            db.execute("Update Empdata SET  EmpAge = "+newage+" where ( EmpEmail = '"+ gmail + "' or EmpUser = '"+ Username +"') and EmpPass = '"+ Password +"';")
                            path.commit()
                            ansEprofileEdit = 7
                            break
                        while ansEprofileEdit == 3:
                            newCountry=input("Enter Country: ")
                            db.execute("Update Empdata SET EmpCountryOR = '"+newCountry+"' where ( EmpEmail = '"+ gmail + "' or EmpUser = '"+ Username +"') and EmpPass = '"+ Password +"';")
                            path.commit()
                            ansEprofileEdit = 7
                            break
                        while ansEprofileEdit == 4:
                            newcity=input("Enter City: ")
                            db.execute("Update Empdata SET  EmpCityOR = '"+newcity+"' where ( EmpEmail = '"+ gmail + "' or EmpUser = '"+ Username +"') and EmpPass = '"+ Password +"';")
                            path.commit()
                            ansEprofileEdit = 7
                            break
                        while ansEprofileEdit == 5:
                            newPhoneno=input("Enter Age: ")
                            db.execute("Update Empdata SET  EmpPhoneno = '"+newPhoneno+"' where ( EmpEmail = '"+ gmail + "' or EmpUser = '"+ Username +"') and EmpPass = '"+ Password +"';")
                            path.commit()
                            ansEprofileEdit = 7
                            break
                        while ansEprofileEdit == 6:
                            newpass=input("Enter Password: ")
                            db.execute("Update Empdata SET EmpPass = '"+newpass+"' where ( EmpEmail = '"+ gmail + "' or EmpUser = '"+ Username +"') and EmpPass = '"+ Password +"';")
                            path.commit()
                            db.execute("Update Logindata SET Pass = '"+newpass+"' where ( Email = '"+ gmail + "' or User = '"+ Username +"') and Pass = '"+ Password +"';")
                            path.commit()
                            ansEprofileEdit = 7
                            break
                        break
                    ans_emp=5
                    break
                break
            while ans_emp == 4:
                db.execute("select * from task;")
                tasks=db.fetchall()
                for taskx in tasks :
                    print(taskx[2],taskx[0],"||",taskx[1])
                ans_emp=5
                break
            break
        continue
    if Accspecs == 'STORE':
        print("""

|SELECT|
___________________________
| 1 | Veiw Customer List  |
| 2 | Veiw Employee List  |
| 3 | Assign Tasks        |  
| 4 | Veiw Product List   |
| 5 | Veiw Store Details  |
| 6 | Exit                |
~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
        ans_store=int(input("==>"))
        while ans_store == 6:
            a=1
            break
        while ans_store != 6:
            while ans_store == 1:
                db.execute(" Select Max(Length(Custname)), max(length(CustEmail)), max(length(CustCardcolour)) from Custdata;")
                length = db.fetchone()
                db.execute("Select Custname, CustEmail, CustCardcolour from Custdata")
                custdetails=db.fetchall()
                print("_"*157)
                for custdata in custdetails :
                    Pcust="{:<3} {:<"+str(length[0]+2)+"} {:<3} {:<"+str(length[1]+2)+"} {:<3} {:<"+str(length[2]+2)+"}{:<3}"
                    print(Pcust.format("|",custdata[0],"|",custdata[1],"|",custdata[2],"|"))
                print("~"*157)
                ans_store = 6
                break
            while ans_store == 2:
                db.execute("SELECT StoreName from Storedata where ( StoreEmail = '"+ gmail + "' or StoreUser = '"+ Username +"') and StorePass = '"+ Password +"';")
                Sname=db.fetchone()
                db.execute(" Select Max(Length(S_No)), max(length(EmpEmail)), max(length(EmpUser)), max(length(Empname)), max(length(EmpAge)), max(length(EmpCountryOR)), max(length(EmpCityOR)), max(length(EmpDateofentry)), max(length(EmpTimeofentry)), max(length(EmpDateOB)), max(length(EmpPhoneno)), max(length(EmpCardcolour)), max(length(EmpPoints)), max(length(EmpGender)), max(length(EmpStore)) from Empdata where Empstore = '"+Sname[0]+"' ;")
                emp_len=    db.fetchone()
                db.execute("SELECT S_No, EmpEmail, EmpUser, Empname, EmpAge, EmpCountryOR, EmpCityOR, EmpDateofentry, EmpTimeofentry, EmpDateOB, EmpPhoneno, EmpCardcolour,EmpPoints, EmpGender, EmpStore from Empdata where Empstore = '"+Sname[0]+"' ;")
                emp_details=db.fetchall()
                print("_"*157)
                for empdata in emp_details:
                    Pemp="{:<3} {:<"+str(emp_len[0]+2)+"} {:<3} {:<"+str(emp_len[3]+2)+"} {:<3} {:<"+str(emp_len[2]+2)+"} {:<3} {:<"+str(emp_len[1]+2)+"} {:<3} {:<"+str(emp_len[4]+2)+"} {:<3} {:<"+str(emp_len[13]+2)+"} {:<3} {:<"+str(emp_len[5]+2)+"} {:<3} {:<"+str(emp_len[6]+2)+"} {:<3} {:<"+str(emp_len[7]+2)+"} {:<3} {:<"+str(emp_len[8]+2)+"} {:<3} {:<"+str(emp_len[9]+2)+"} {:<3} {:<"+str(emp_len[10]+2)+"} {:<3} {:<"+str(emp_len[11]+2)+"} {:<3} {:<"+str(emp_len[12]+2)+"} {:<3}"
                    print(Pemp.format("|",empdata[0],"|",empdata[3],"|",empdata[2],"|",empdata[1],"|",empdata[4],"|",empdata[13],"|",empdata[5],"|",empdata[6],"|",str(empdata[7]),"|",str(empdata[8]),"|",str(empdata[9]),"|",str(empdata[10]),"|",empdata[11],"|",empdata[12],"|"))
                ans_store = 6
                print("~"*157)
                break
            while ans_store == 3:
                db.execute("SELECT StoreName from Storedata where ( StoreEmail = '"+ gmail + "' or StoreUser = '"+ Username +"') and StorePass = '"+ Password +"';")
                Sname=db.fetchone()
                db.execute(" Select Max(Length(S_No)), max(length(EmpEmail)), max(length(EmpUser)), max(length(Empname)), max(length(EmpAge)), max(length(EmpCountryOR)), max(length(EmpCityOR)), max(length(EmpDateofentry)), max(length(EmpTimeofentry)), max(length(EmpDateOB)), max(length(EmpPhoneno)), max(length(EmpCardcolour)), max(length(EmpPoints)), max(length(EmpGender)), max(length(EmpStore)) from Empdata where Empstore = '"+Sname[0]+"' ;")
                emp_len=db.fetchone()
                db.execute("SELECT S_No, EmpEmail, EmpUser, Empname, EmpAge, EmpCountryOR, EmpCityOR, EmpDateofentry, EmpTimeofentry, EmpDateOB, EmpPhoneno, EmpCardcolour,EmpPoints, EmpGender, EmpStore from Empdata where Empstore = '"+Sname[0]+"' ;")
                emp_details=db.fetchall()
                print("_"*157)
                s_no=[]
                for empdata in emp_details:
                    s_no.append(empdata[0])
                    Pemp="{:<3} {:<"+str(emp_len[0]+2)+"} {:<3} {:<"+str(emp_len[3]+2)+"} {:<3} {:<"+str(emp_len[2]+2)+"} {:<3} {:<"+str(emp_len[1]+2)+"} {:<3} {:<"+str(emp_len[4]+2)+"} {:<3} {:<"+str(emp_len[13]+2)+"} {:<3} {:<"+str(emp_len[5]+2)+"} {:<3} {:<"+str(emp_len[6]+2)+"} {:<3} {:<"+str(emp_len[7]+2)+"} {:<3} {:<"+str(emp_len[8]+2)+"} {:<3} {:<"+str(emp_len[9]+2)+"} {:<3} {:<"+str(emp_len[10]+2)+"} {:<3} {:<"+str(emp_len[11]+2)+"} {:<3} {:<"+str(emp_len[12]+2)+"} {:<3}"
                    print(Pemp.format("|",empdata[0],"|",empdata[3],"|",empdata[2],"|",empdata[1],"|",empdata[4],"|",empdata[13],"|",empdata[5],"|",empdata[6],"|",str(empdata[7]),"|",str(empdata[8]),"|",str(empdata[9]),"|",str(empdata[10]),"|",empdata[11],"|",empdata[12],"|"))
                print("~"*157)
                print("""|Please Enter The Serial Number of the Person You wish to Assign the Task|""")
                ans_task = int(input("==>"))
                while ans_task in s_no:
                    db.execute("Select Empname from Empdata where S_No = "+str(ans_task)+"    ;")
                    name=db.fetchone()
                    db.execute("Select StoreName from Storedata where ( StoreEmail = '"+ gmail + "' or StoreUser = '"+ Username +"') and StorePass = '"+ Password +"';")
                    name2=db.fetchone()
                    taskx=input("TASK  ==> ")
                    db.execute("Insert into task (Task ,Status,StoreName,Empname) values ( '{}','{}','{}','{}');".format(taskx,'Pending',name2[0],name[0]))
                    path.commit()
                    ans_task= max(s_no) + 5
                    break
                break
            while ans_store == 4:
                db.execute("SELECT StoreName from Storedata where ( StoreEmail = '"+ gmail + "' or StoreUser = '"+ Username +"') and StorePass = '"+ Password +"';")
                Sname=db.fetchone()
                db.execute("Select MAX(LENGTH(S_No)),MAX(LENGTH(ProdName)),MAX(LENGTH(ProdCompany)),MAX(LENGTH(ProdCode)),MAX(LENGTH(ProdCategory)),MAX(LENGTH(ProdPrice_inr)) from Productsdata where StoreName = '"+Sname[0]+"' ;")
                numlist=db.fetchone()
                db.execute("Select * from Productsdata where StoreName = '"+Sname[0]+"';")
                Products=db.fetchall()
                print("_"*157)
                for row in Products:
                    Pprod="{:<3} {:<"+str(numlist[0]+2)+"} {:<3} {:<"+str(numlist[1]+2)+"} {:<3} {:<"+str(numlist[2]+2)+"} {:<3} {:<"+str(numlist[3]+2)+"} {:<3} {:<"+str(numlist[4]+2)+"} {:<3} {:<"+str(numlist[5]+2)+"} {:<3}"
                    print(Pprod.format("|",str(row[0]),"|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",str(row[5]),"|"))
                print("~"*157)
                print("""
|SELECT|
______________________
| 1 | Add Product    |
| 2 | Delete Product |
| 3 | Exit           |
~~~~~~~~~~~~~~~~~~~~~~
""")
                ans_sprod=int(input("==>"))
                while ans_sprod == 1:
                    Pname=input("Enter Product Name :")
                    Pcompany=input("Enter Product Company :")
                    Pcode=(Pname[0]+ Pcompany[0] + Sname[0][0])+str(len((Pname+ Pcompany + Sname[0])))
                    Pcategory=input("Enter Product Category :")
                    Pprice=int(input("Enter Price (in Inr) :"))
                    db.execute("Insert into Productsdata (ProdName ,ProdCompany ,ProdCode ,ProdCategory ,ProdPrice_inr,StoreName) values ( '{}','{}','{}','{}','{}','{}');".format(Pname,Pcompany,Pcode,Pcategory,Pprice,Sname[0]))
                    path.commit()
                    ans_spord=3
                    break
                while ans_sprod == 2:
                    Pcode=input("Enter the Product Code Of the Product You want to Delete ==>")
                    db.execute("DELETE from Cart where ProdCode = '"+Pcode+"';")
                    path.commit()
                    db.execute("DELETE from Productsdata where ProdCode = '"+Pcode+"';")
                    path.commit()
                    ans_spord=3
                    break
                if ans_sprod == 3:
                    ans_store=6
                    break
                break
            while ans_store==5:
                db.execute("SELECT * from Storedata where ( StoreEmail = '"+ gmail + "' or StoreUser = '"+ Username +"') and StorePass = '"+ Password +"';")
                S_details=db.fetchone()
                print("_"*157)
                print("| Name : ", S_details[2] )
                print("| Username : ", S_details[5] )
                print("| Email : " ,S_details[1] )
                print("| Country Of Residence : ", S_details[3] )
                print("| City Of Residence : ", S_details[4] )
                print("| Registration Date : ", S_details[8] )
                print("| Regitration Time : ", S_details[9] )
                print("| Date Of Establishment : ", S_details[7] )
                print("| Phone Number : ", S_details[10] )
                print("~"*157)
                print()
                print()
                print("|SELECT|")
                print("""
______________________
| 1 | Update Profile |
| 2 | Exit           |
~~~~~~~~~~~~~~~~~~~~~~
""")
                ansstrprofile=int(input("==>"))
                while ansstrprofile == 1:
                    print("""
|SELECT to Update|
_____________________                    
| 1 | Email         | 
| 2 | Phone Number  |
| 3 | Password      |
| 4 | Exit          |
~~~~~~~~~~~~~~~~~~~~~
""")
                    ansSprofileEdit=int(input("==>"))
                    while ansSprofileEdit < 4:
                        while ansSprofileEdit == 1:
                            newmail=input("Enter New Email : ")
                            db.execute("Update Storedata SET StoreEmail = "+newmail+" where ( StoreEmail = '"+ gmail + "' or StoreUser = '"+ Username +"') and StorePass = '"+ Password +"';")
                            path.commit()
                            db.execute("Update Logindata SET Email = "+newmail+" where ( Email = '"+ gmail + "' or User = '"+ Username +"') and Pass = '"+ Password +"';")
                            path.commit()
                            ansSprofileEdit = 4
                            break
                        while ansSprofileEdit == 2:
                            newPhoneno=input("Enter Phone Number: ")
                            db.execute("Update Storedata SET  StorePhoneno = "+newPhoneno+" where ( StoreEmail = '"+ gmail + "' or StoreUser = '"+ Username +"') and StorePass = '"+ Password +"';")
                            path.commit()
                            ansSprofileEdit = 4
                            break
                        while ansSprofileEdit == 1:
                            newpass=input("Enter New Password : ")
                            db.execute("Update Storedata SET StorePass = "+newpass+" where ( StoreEmail = '"+ gmail + "' or StoreUser = '"+ Username +"') and StorePass = '"+ Password +"';")
                            path.commit()
                            db.execute("Update Logindata SET Pass = "+newpass+" where ( Email = '"+ gmail + "' or User = '"+ Username +"') and Pass = '"+ Password +"';")
                            path.commit()
                            ansSprofileEdit = 4
                            break
                    if ansSprofileEdit > 3:
                        ansstrprofile = 2
                        break
                if ansstrprofile > 1:
                    ans_store=6
                    break
                break
            break
        continue
    os.system('clear')
    break

