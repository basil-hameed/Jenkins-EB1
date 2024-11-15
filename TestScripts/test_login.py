"""
test_login.py contains the test cases

Test Scripts File
"""
from PageObjects.LoginPage import HRMLoginPage

# test case for starting automation
def test_start():
    assert HRMLoginPage().start() == True
    print("SUCCESS : Automation started!")

# test case for login orange hrm
def test_login():
    assert HRMLoginPage().login() == True
    print("SUCCESS : Logged In!")

# test case for shutdown the browser
def test_shutdown():
    assert HRMLoginPage().shutdown() == None  
    print("SUCCESS : Automation shutdown!")
