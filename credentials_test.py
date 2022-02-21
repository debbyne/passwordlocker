import unittest
from credentials import Credentials
from passwordlocker import User

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the Credentials class.
    Args:
    unittest.TestCase:TestCase that helps in creating test  cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Instagram" "Devian","1234")
    def tearDown(self):
        '''
        tearDown cleans up after each test case is run
        '''
        Credentials.credentials_list = [] 
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''


        self.assertEqual(self.new_credential.account, "instagram")
        self.assertEqual(self.new_credentials.user_name, "Devian")
        self.assertEqual(self.new_credentials.pass_word, "1234")
    
    def test_log_in(self):
        '''
        this test checks whether user can login into accounts using their credentials
        '''
        self.new_user.save_user()

        test_user = User("Devian",)

        test_user.save_user()

        found_credentials = User.log_in("Devian",)

        self.assertEqual(found_credentials, Credentials.credentials_list) 