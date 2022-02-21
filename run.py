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
    User.save_user()
def check_existing_users(name):
    '''
    function that checks if a user account name already exists
    '''

    return User.user_exist(name)
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
    credentials.save_credentials()
def delete_credential(Credential):
    '''
    function to delete a credential
    ''' 
    Credential.delete_credential 
def display_credentials(Credential):
    ''' 
    function that displays existing credentials
    '''
    return Credential.credentials_list


























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



                
