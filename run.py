from passwordlocker import User
from credentials import Credentials
def main():
    '''
    method that controls the passwordlocker
    '''
    print("Hello Welcome to passwordlocker.")
    

    print(f"Hello you have two options")

    while True:
                print(
                    '''
                1.Create a new account
                2.Login to your existing account
                ''' )
                number = input()
                if number == "1":
                    '''
                    Create a new account
                    '''
                    print("Enter user_name...")
                    user_name = input()
                    print()

                
