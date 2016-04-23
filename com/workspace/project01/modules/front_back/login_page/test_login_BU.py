'''
Created on Apr 15, 2016

@author: ZinhVcoin
'''
import pytest
import allure
from com.workspace.project01.modules.AbstractTest import AbstractTest
import os

@allure.feature('Login')
class Test_login_BU(AbstractTest):
    
    EmptyPasswordErrorMessage = "Empty password not allowed"
    UsernameAndPasswordNotMacthMessage = "Username and password do not match or you do not have an account yet."
    
    @pytest.fixture(scope = "module", autouse=True)
    def pre_condition(self, request):
        self.logInfo("Navigate to Joomla Login page")
        self.loginPage().navigateToWeb(self.cfJoomlaURL, self.cfDriver)
         
        def post_condition():
            self.logInfo("Close Joomla page")
            self.loginPage().closeBrowser()
             
        request.addfinalizer(post_condition)
    
    @allure.story("Functional")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.allure.testcase("Verify user can't login with empty username and password")
    @pytest.mark.us
    def test_tc001(self):
        self.logInfo("1. Leave username and password blank")
        self.logInfo("2. Click Login button")
        self.loginPage().login("", "")
        
        self.logInfo("3. Verify the 'Empty password not allowed' error message is displayed")
        self.loginPage().checkErrorMessageDisplayed(self.EmptyPasswordErrorMessage)
        
    @allure.story("Functional")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.allure.testcase("Verify user can't login with empty password")
    def test_tc002(self):
        self.logInfo("1. Enter username")
        self.logInfo("2. Leave password blank")
        self.logInfo("3. Click Login button")
        self.loginPage().login(self.cfValidUsername, "")
         
        self.logInfo("3. Verify the 'Empty password not allowed' error message is displayed")
        self.loginPage().checkErrorMessageDisplayed(self.EmptyPasswordErrorMessage)
     
    @allure.story("Functional")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.allure.testcase("Verify user can't login with empty username")
    def test_tc003(self):
        self.logInfo("1. Leave username blank")
        self.logInfo("2. Enter password")
        self.logInfo("3. Click Login button")
        self.loginPage().login("", self.cfValidPassword)
         
        self.logInfo("3. Verify the 'Username and password do not match or you do not have an account yet.' error message is displayed")
        self.loginPage().checkErrorMessageDisplayed(self.UsernameAndPasswordNotMacthMessage)
     
    @allure.story("Functional")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.allure.testcase("Verify user can't login with invalid account")
    def test_tc004(self):
        self.logInfo("1. Enter invalid username")
        self.logInfo("2. Enter invalid password")
        self.logInfo("3. Click Login button")
        self.loginPage().login(self.cfInvalidUsername, self.cfInvalidPassword)
         
        self.logInfo("3. Verify the 'Username and password do not match or you do not have an account yet.' error message is displayed")
        self.loginPage().checkErrorMessageDisplayed(self.UsernameAndPasswordNotMacthMessage)
     
    @allure.story("Functional")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.allure.testcase("Verify user can login with valid account")
    def test_tc005(self):
        self.logInfo("1. Enter valid username")
        self.logInfo("2. Enter valid password")
        self.logInfo("3. Click Login button")
        self.loginPage().login(self.cfValidUsername, self.cfValidPassword)
         
        self.logInfo("3. Verify control panel page is displayed")
        self.controlPanelPage().checkPageIsDisplayed()

if __name__ == "__main__":
    pytest.main()