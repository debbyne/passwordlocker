from unicodedata import numeric
import unittest
from passwordlocker import User
class  Credentials:
    '''
    class that generates new instances of credentials
    '''
    credentials_list =[]
    def __init__(self,account,credentialsuser_name,credentialspass_word):
        '''
        method that helps define properties for our object self
        '''
        self.account = account
        self.credentialsuser_name = credentialsuser_name
        self.credentialspass_word = credentialspass_word

    def save_credentials(self):
         '''
        this method saves user info into accounts
         ''' 
         Credentials.credentials.append(self)  
    def create_credentials(self):
        print("Add user_name")
        print("/n")
        user_name =input("user_name: ")
        print("Insert new pass_word")
        pass_word = input("pass_word: ")
    def delete_credentials(self):
        '''
        this method deletes saved credentials from accounts
        '''
        Credentials.credentials.remove(self)
    @classmethod 
    def display_credentials(cls):  
        '''
        this method returns list of credentials
        ''' 
        # for account in cls.accounts:
        return cls.credentials_list
    @classmethod
    def generate_pass_word(cls):
       '''
       method that generates password
       '''
       length = 4
       numeric
       return pass_word
       print(pass_word)
    @classmethod
    def log_in(cls,name,password):
        '''
        this method enables users to log into their acccounts
        '''
        for user in cls.user_list:
            if User.user_name ==name and User.pass_word ==password:
                return Credentials.credentials_list
    def delete_credentials(self):
        '''
        this method deletes saved credentials from accounts
        '''

