import mysql.connector as connector

# Database Connector


class DBHelper:
    def __init__(self):
        self.con = connector.connect(host="localhost", port='3306', user='root',
                                     password='password', database='DBMSProject', auth_plugin='mysql_native_password')
        query = "create table if not exists user(userID int primary key,userName varchar(200),phone bigint,Account_No bigint, Available_Balance bigint,Loan bigint)"
        cur = self.con.cursor()
        cur.execute(query)


# Insert Users into Database

    def insert_user(self, userId, userName, phone, Account_No, Available_Balance, Loan):
        query = "insert into user(userId,userName,phone,Account_No,Available_Balance,Loan) values ({},'{}',{},{},{},{})".format(
            userId, userName, phone, Account_No, Available_Balance, Loan)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("New user is saved in Database")
        print()


# Fetch all Data in the database

    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        print("Showing Users in the database: ")
        print()
        for row in cur:
            print("User Id:", row[0])
            print("User Name:", row[1])
            print("User Phone No:", row[2])
            print("User Account No:", row[3])
            print("Available Balance:", row[4])
            print("Loan Taken:", row[5])
            print()
            print()


# Delete user by using id

    def delete_user(self, userId):
        query = "delete from user where userId={}".format(userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User successfully deleted from database")
        print()


# Update data of user by using id

    def update_user(self, userId, newName, newPhoneNo, newAccountNo, newAvailableBalance, LoanTaken):
        query = "update user set userName='{}',phone={},Account_No={},Available_Balance={},Loan={} where userId={}".format(
            newName, newPhoneNo, newAccountNo, newAvailableBalance, LoanTaken, userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User data is updated successfully")
        print()
