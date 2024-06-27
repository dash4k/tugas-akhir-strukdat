import unittest
import os
import pickle
from account import Account, DataAccount  # Replace 'your_module' with the actual module name

class TestDataAccount(unittest.TestCase):
    
    def setUp(self):
        # Initialize a test instance of DataAccount
        self.data_account = DataAccount()
        
        # Sample data for testing
        self.sample_data1 = {"nama": "John Doe", "alamat": "123 Main St", "tipe_pembayaran": "Cash", "umur": 30}
        self.sample_data2 = {"nama": "Jane Smith", "alamat": "456 Elm St", "tipe_pembayaran": "Insurance", "umur": 25}
        
        # Sample accounts for testing
        self.account1 = Account("john_doe", "password123", 1)
        self.account1.data = self.sample_data1
        
        self.account2 = Account("jane_smith", "password456", 1)
        self.account2.data = self.sample_data2
    
    def tearDown(self):
        # Clean up after each test if necessary
        if os.path.exists("database.pkl"):
            os.remove("database.pkl")
    
    def test_add_account(self):
        # Test adding an account
        self.data_account.add_account(self.sample_data1, self.account1)
        
        # Assert that the head is not None after adding an account
        self.assertIsNotNone(self.data_account.head)
        
        # Test adding another account
        self.data_account.add_account(self.sample_data2, self.account2)
        
        # Assert that the head and tail are different after adding multiple accounts
        self.assertNotEqual(self.data_account.head, self.data_account.tail)
    
    def test_remove_account(self):
        # Add an account first
        self.data_account.add_account(self.sample_data1, self.account1)
        
        # Test removing an account
        self.assertTrue(self.data_account.remove_account("john_doe"))
        
        # Assert that the head is None after removing the only account
        self.assertIsNone(self.data_account.head)
    
    def test_login(self):
        # Add an account first
        self.data_account.add_account(self.sample_data1, self.account1)
        
        # Test login with correct username and password
        logged_in_account = self.data_account.login("john_doe", "password123")
        self.assertEqual(logged_in_account.username, "john_doe")
        
        # Test login with incorrect password
        self.assertFalse(self.data_account.login("john_doe", "wrong_password"))
        
        # Test login with non-existing username
        self.assertFalse(self.data_account.login("non_existing_user", "password123"))
    
    # def test_list_pasien(self):
    #     # Add accounts first
    #     self.data_account.add_account(self.sample_data1, self.account1)
    #     self.data_account.add_account(self.sample_data2, self.account2)
        
    #     # Test listing patients
    #     patients_list = self.data_account.list_pasien()
        
    #     # Assert that the length of the list matches the number of patient accounts added
    #     self.assertEqual(len(patients_list), 2)
        
    #     # Assert that the patient info matches the expected structure
    #     self.assertEqual(patients_list[0], ["john_doe", "John Doe", "123 Main St", "Cash", 30])
    #     self.assertEqual(patients_list[1], ["jane_smith", "Jane Smith", "456 Elm St", "Insurance", 25])

    def test_save_and_load_data(self):
        # Add accounts first
        self.data_account.add_account(self.sample_data1, self.account1)
        self.data_account.add_account(self.sample_data2, self.account2)
        
        # Save data to file
        self.assertTrue(self.data_account.save_data())
        
        # Clear existing DataAccount instance
        self.data_account = None
        
        # Create new instance and load data
        new_data_account = DataAccount()
        self.assertTrue(new_data_account.load_data())
        
        # Test if loaded data matches the original accounts
        logged_in_account1 = new_data_account.login("john_doe", "password123")
        self.assertEqual(logged_in_account1.username, "john_doe")
        
        logged_in_account2 = new_data_account.login("jane_smith", "password456")
        self.assertEqual(logged_in_account2.username, "jane_smith")
        

if __name__ == "__main__":
    unittest.main()

