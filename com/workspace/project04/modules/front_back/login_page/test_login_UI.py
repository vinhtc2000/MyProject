'''
Created on Apr 15, 2016

@author: ZinhVcoin
'''
import pytest
import allure
from com.workspace.project01.modules.AbstractTest import AbstractTest
import os

@allure.feature('Login')
class Test_login_UI(AbstractTest):
    
    @pytest.fixture(scope = "module", autouse=True)
    def pre_condition(self, request):
        self.logInfo("Navigate to Joomla Login page")
        self.loginPage().navigateToWeb(self.cfJoomlaURL, self.cfDriver)
         
        def post_condition():
            self.logInfo("Close Joomla page")
            self.loginPage().closeBrowser()
             
        request.addfinalizer(post_condition)
    
    @allure.story("UI")
    @pytest.allure.severity(pytest.allure.severity_level.MINOR) # @UndefinedVariable
    @pytest.allure.testcase("Verify username textbox, password textbox and login button are displayed")
    def test_tc006(self):
        self.logInfo("1. Verify username textbox is displayed")
        self.loginPage().checkUsernameTextboxDisplayed()
        
        self.logInfo("2. Verify password textbox is displayed")
        self.loginPage().checkPasswordTextboxDisplayed()
        
        self.logInfo("3. Verify login button is displayed")
        self.loginPage().checkLoginButtonDisplayed()
    
    @allure.story("UI")
    @pytest.allure.severity(pytest.allure.severity_level.MINOR) # @UndefinedVariable
    @pytest.allure.testcase("Verify username textbox, password textbox and blanked as default")
    def test_tc007(self):
        self.logInfo("1. Verify username textbox is blanked as default")
        self.loginPage().checkUsernameTextboxIsBlanked()
        
        self.logInfo("2. Verify password textbox is blanked as default")
        self.loginPage().checkPasswordTextboxIsBlanked()
        
if __name__ == "__main__":
    pytest.main()