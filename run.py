import string
import random
from passwordlocker import User
from credentials import Credentials
def create_user_account(user_name , pass_word):
    '''
    function to create a user account
    '''
    new_user = User(user_name ,pass_word)
    return new_user
def save_users(user):
    '''
    function thats saves a new user account
    '''    
    return User.save_user()
def check_existing_users(name):
    '''
    function that checks if a user account name already exists
    '''

    return User.user_exists(name)
def display_user(cls):
    '''
    function that returns the user list
    '''
    return cls.user_list
def log_in(user_name,pass_word):
    '''
    this function enables users to log into their acccounts
     '''
    log_in=User.log_in(user_name,pass_word)
    if log_in!=False:
        return User.log_in(user_name,pass_word)
def create_credentials(Credential,account,credentialuser_name,credentialpass_word):   

     '''
     function that creates credentials
     '''
     new_credential = Credential(account,credentialuser_name, credentialpass_word)
     return new_credential
def save_credentials(credentials):
    '''
    function that addes a new credential to the credentials
    '''
    return Credentials.save_credentials()
def del_credential(name):
    '''
    function to delete a credential
    ''' 
    return Credentials.delete_credential(name)
def display_credentials():
    ''' 
    function that displays existing credentials
    '''
    return Credentials.display_credentials()
def main():
    '''
    function that controls the passwordlocker
    '''
    print("WELCOME TO PASSWORD LOCKER.")
    

    print("you have two options")

    while True:
                print('''
                1.Create a new account
                2.Login to your existing account
                ''')
                number = input()
                if number == "1":
                    '''
                    Create a new account
                    '''
                    print("Enter username of choice...")
                    user_name = input()
                    print("""
                    1.Create your own password
                    2.Generate password
                    """ )
                    
                    def gen_password():
                        number = input()
                        if number =="1":
                            print("Enter password...")
                            passwrd = input()   
                        elif number == "2":
                            print("(Generate password...")
                            length = int(input("\nEnter the length of your desired password: "))
                            lower = string.ascii_lowercase
                            num = string.digits
                            all = lower + num

                            generate_password = random.sample(all, length)

                            generated_password = "".join(generate_password)

                            print("Your password has been auto-generated")
                            print(generated_password)
                    gen_password()

                elif number == "2":
                    '''
                    user logs in to existing account
                    '''
                    print("Enter username...")
                    username = input()
                    print('\n')
                    print("Enter password")
                    password = input()
                    print('\n')
                    print("Welcome to your password locker account ")
                    while True:
                        '''
                        After logging in
                        '''
                        print('''
                               1.Create a new credential
                               2.Use generated credential
                               3.Display existing account credentials
                               4.Delete user account
                            ''')
                        number = input()
                        if number =="1":
                             '''
                             Create your own account using your own password
                             '''
                             print("Enter account name:...")
                             account = input()
                             print("Enter the username:...")
                             credential_username = input()
                             print("Enter the password:...")
                             credential_password = input()
                             save_credential( create_credential(account,credential_username,credential_password))
                             print(f"Your {account} credentials have been successfully created!")
                        elif number =="2":
                             '''
                             Create account using generated password
                             '''
                             print("Enter account name:...")
                             account = input()
                             print("Enter the username:...")
                             credential_username = input()
                             save_credential(create_credential(account, credential_username, (generating_password())))  
                             print(f"Your {account} credentials have been successfully created!")
                        elif number =="3":
                            '''
                            display existing details
                            '''
                            if display_credentials():
                                print("List of existing credentials")
                                for credentials in display_credentials():
                                    print(f"Account-{credentials.account}")
                                    print(f"Username- {credentials.credentialsuser_name}") 
                                    print(f"Password- {credentials.credentialspass_word}")  

                                else:
                                    print("Wrong input")
                        
                        elif number == "4":
                            """
                            Delete user 
                            """
                            print("Enter username for account to be deleted")
                            deleting_credentils = input()
                            if check_existing_users(deleting_credentils):
                                del_credential(check_existing_users(deleting_credentils))
                                print("Account Deleted successfully")

                            else:
                                print("Account does not exist")




                        else:
                            print("You have no saved credentials")

if __name__ =='__main__':
    main()





                
