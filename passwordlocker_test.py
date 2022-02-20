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
        self.new_user = User("Devian",1234)
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
    
if __name__ =='__main__':
    unittest.main()
       