class User:
    """
    Class that creates the password locker account
    """
    user_list = []
    def __init__(self,username,password):
        '''
           __init__ method that helps us define properties for our objects.
        '''
    
        self.username = username
        self.password = password