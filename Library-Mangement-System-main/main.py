import Login as L
import LinkList as U

import booklogo as B
import os

def mainfun():
    pic = B.bookpic[0]
    print(pic)

    while True:
        menu = B.menu[0]
        print(menu)
        useroradmin = input('''
     | |-------------|
     | | Enter Here  |
     | |-------------| >>''')
        os.system("clear")
        pic = B.bookpic[0]
        print(pic)

        if useroradmin == '1':
            
          
            login = B.userlogin[0]
            print(login)
            UserName = input    ('''
     | |-------------|
     | | Enter Here  |
     | |-------------| >>''')
            UserID =  input     ('''
     | |-------------|
     | | Enter Here  |
     | |-------------| >>''')
            Userpassword = input('''
     | |-------------|
     | | Enter Here  |
     | |-------------| >>''')
            print("\n")
            os.system("clear")
            pic = B.bookpic[0]
            print(pic)

            PermissionUser = L.User_login_check(UserName,Userpassword,UserID)

            if PermissionUser == True:
                while True:
                    os.system("clear")
                    pic = B.bookpic[0]
                    print(pic)
                    peruser = B.userfunc[0]
                    print(peruser)
                    choice = input('''
     | |-------------|
     | | Enter Here  |
     | |-------------| >>''')
                    if choice == '5':
                        break

                    U.userfunc(choice,UserID)
            else:
                print('''
     |--------------------------------|
     | Invalid User Name or Password  |
     |--------------------------------|\n
                      '''
                    )

        elif useroradmin == '2':

            admin = B.adminlogin[0]
            print(admin)
            Adminid = input('''
     | |-------------|
     | | Enter Here  |
     | |-------------| >>''' )
            Adminpass = input('''
     | |-------------|
     | | Enter Here  |
     | |-------------| >>''')
            os.system("clear")
            pic = B.bookpic[0]
            print(pic)
            PermissionAmdin = L.Admin_login_check(Adminid,Adminpass)

            if PermissionAmdin == True:
                while True:
                    os.system("clear")
                    pic = B.bookpic[0]
                    print(pic)
            
                    adminfun = B.adminfunc[0]
                    print(adminfun)
                    choice = input('''
     | |-------------|
     | | Enter Here  |
     | |-------------| >>''')
                    print("\n")
                    if choice == '7':
                        break
                    U.AdminFunc(choice)
            else:
                print(
                    '''
     |--------------------------------|
     | Invalid User Name or Password  |
     |--------------------------------|\n
                    '''
                    )
        elif useroradmin == '3':
            L.Register_User()
        elif useroradmin == '4':
            break
        else:
            print(
                '''
     |----------------|
     | Invalid Input  |
     |----------------|\n
                ''')

while True:
    mainfun()
    confirmexit = input('''
     |-------------------------------------|
     | Are You Sure You Want to Exit (Y/N) |
     |-------------------------------------|>>''')
    if confirmexit == 'Y':
        break
os.system("clear")
print(B.exitlib[0])

