class  Credentials:
    '''
    class that generates new instances of credentials
    '''
    accounts =[]
    def __init__(self,accountuser_name,accountpass_word):
        '''
        method that helps define properties for our object self
        '''

        self.accountuser_name = accountuser_name
        self.accountpass_word = accountpass_word

    def save_account(self):
         '''
        this method saves user info into accounts
         ''' 
         Credentials.accounts.append(self)  
    def create_account(self):
        print("Add user name")
        print("/n")
        user_name =input("user name: ")
        print("Insert new password")
        pass_word = input("password: ")
    def delete_account(self):
        '''
        this method deletes saved credentials from accounts
        '''
        Credentials.accounts.remove(self)
    @classmethod 
    def display_accounts(cls,name):  
        '''
        this method returns list of accounts
        ''' 
        for account in cls.accounts:
            return cls.user_list
    @classmethod
    def generate_password(cls):
       '''
       method that generates password
       '''
       length = 4
       
