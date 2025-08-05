import unittest
import json
import requests
import datetime

def validate_email(email):
    # 이메일 검증
    if "@" in email and "." in email:
        return True
    else:
        return False

class API_Handler:
    def __init__(self):
        self.base_url = "https://api.example.com"
        self.timeout = 30
        
    def send_request(self, endpoint, data):
        try:
            response = requests.post(f"{self.base_url}/{endpoint}", 
                                   json=data,
                                   timeout=self.timeout)
            return response.json()
        except:
            return None
            
    def process_user_registration(self, user_data):
        if not validate_email(user_data.get("email", "")):
            raise ValueError("Invalid email")
            
        # 사용자 등록 처리
        result = self.send_request("register", user_data)
        if result:
            print("Registration successful")
            return True
        else:
            print("Registration failed")
            return False

class TestEmailValidation(unittest.TestCase):
    def test_valid_email(self):
        # Test with valid email
        self.assertTrue(validate_email("test@example.com"))
        
    def test_invalid_email_no_at(self):
        # Test email without @
        result = validate_email("testexample.com")
        self.assertFalse(result)
        
    def testInvalidEmailNoDot(self):
        self.assertFalse(validate_email("test@example"))

def get_user_input():
    email = input("Enter email: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    
    return {
        "email": email,
        "name": name,
        "age": int(age) if age.isdigit() else 0
    }

if __name__ == "__main__":
    handler = API_Handler()
    
    try:
        user_data = get_user_input()
        handler.process_user_registration(user_data)
    except Exception as e:
        print(f"Error: {e}")