import unittest
from passwordlocker import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class.
    Args:
    unittest.TestCase:TestCase that helps in creating test  cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Devian","1234")
        
    def tearDown(self):
        '''
        tearDown cleans up after each test case is run
        '''
        User.user_list = []
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Devian")
        self.assertEqual(self.new_user.pass_word,"1234")

    def test_save_user(self):
        """
        Testing to see if a user gets saved
        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
    
    def test_user_exists(self):
        """
        test to check existance of user
        """

        self.new_user.save_user()
        test_user = User("Devian"," 1234")
        test_user.save_user()
        user_exists = User.user_exists("Devian")
        self.assertTrue(user_exists)
    

    def test_find_user_by_name(self):
        """
        test to find user by username
        """
        self.new_user.save_user()
        test_user = User("ig","Dev")
        test_user.save_user()
        find_user = User.find_user_by_name("ig")
        self.assertEqual(find_user.user_name, test_user.user_name)
        

if __name__ =='__main__':
    unittest.main()
