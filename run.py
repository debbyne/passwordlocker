from passwordlocker import User
from credentials import Credentials
def main():
    '''
    method that controls the passwordlocker
    '''
    print("WELCOME TO PASSWORD LOCKER.")
    

    print(f"you have two options")

    while True:
                print( 
                1.Create a new account
                2.Login to your existing account
                 )
                number = input()
                if number == "1":
                    '''
                    Create a new account
                    '''
                    print("Enter username...")
                    user_name = input()
                    print(
                    1.Create your own password
                    2.Generate password
                    )
                    number = input()
                    if number =="1":
                        print("Enter password...")   
                    elif number == "2":



                
