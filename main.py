from dbHelper import DBHelper


def main():

    db = DBHelper()
    while True:
        print("*************** WELCOME ***************")
        print("Press 1 to display all Users in the Database")
        print("Press 2 to insert a User in the Database")
        print("Press 3 to update a User in the Database")
        print("Press 4 to delete a User in the Database")
        print("Press 5 to exit from the program")
        try:
            choice = int(input())
            if(choice == 1):
                db.fetch_all()
                pass

            elif(choice == 2):
                uid = int(input("Enter user id: "))
                userName = str(input("Enter user name: "))
                userPhoneNo = int(input("Enter user Phone No: "))
                userAccountNo = int(input("Enter user Account No: "))
                availableBalance = int(input("Enter Available Balance: "))
                loan = int(input("Enter loan amount taken from the bank: "))
                db.insert_user(uid, userName, userPhoneNo,
                               userAccountNo, availableBalance, loan)
                pass

            elif(choice == 3):
                uid = int(input("Enter user id: "))
                userName = str(input("Enter new user name: "))
                userPhoneNo = int(input("Enter new user Phone No: "))
                userAccountNo = int(input("Enter new user Account No: "))
                availableBalance = int(input("Enter new available Balance: "))
                loan = int(
                    input("Enter new loan amount taken from the bank: "))
                db.update_user(uid, userName, userPhoneNo,
                               userAccountNo, availableBalance, loan)
                pass

            elif(choice == 4):
                userId = int(
                    input("Enter the user id of the user you want to delete: "))
                db.delete_user(userId)
                pass

            elif(choice == 5):
                print("Program terminated")
                print("bye! See you again!")
                break

            else:
                print("Invalid Input! Try again")
        except Exception as e:
            print("Invalid Input! Try again")


if __name__ == "__main__":
    main()
