import random
from random import randint

#Function for checking the validity userid and password of the admin
def Admin_login_check(checkusername, checkpassword):
    adminusername = "FasihMuhammad"
    adminpassword = "200901012"
    if checkusername == adminusername and checkpassword == adminpassword:
         return True


#Function for checking the validity of the user
def User_login_check(name , password , userid):
    with open("UserInfo.txt", "r") as r:
        while True:
            n = r.readline()
            s = r.readline()
            i = r.readline()
            if not n and not s and not i :
                break
            if n == name + "\n"  and s == password + "\n" and i == userid + "\n" :
                return True
                break

    r.close()

#Function to regeister a user
def Register_User():
    with open("UserInfo.txt","a") as au:
        print(
            '''
     |--------------------------|
     | Welcome For Registration |
     |--------------------------|\n
            '''
            )
        username = input('''
     |-------------------|
     |  Enter a UserName |
     |-------------------|>>''')
        au.write(username + "\n")
        userpassword = input('''
     |------------------|
     | Enter a Password |
     |------------------|>>''')
        au.write(userpassword + "\n")
        userid = random.randint(0,5000)
        au.write(str(userid) + "\n")
        print(
            f'''
     |-----------------------------------------------------|
     | Your User ID is {userid} , Dont forgrt your user Id |
     |-----------------------------------------------------|
             ''')
    au.close()
