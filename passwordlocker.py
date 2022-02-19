class User:
    """
    Class that creates the password locker account
    """
    user_list = []
    def __init__(self,user_name,pass_word):
        '''
           __init__ method that helps us define properties for our object.
           user_name :name of user
           user_password : password for a user
        '''
    
        self.user_name = user_name
        self.pass_word = pass_word

    def save_user(self):
         '''
        this method adds a new user to the user list
         '''   
         User.user_list.append(self)  
    @classmethod
    def user_exist()    
