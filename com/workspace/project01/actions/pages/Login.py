'''
Created on Apr 15, 2016

@author: ZinhVcoin
'''

from com.workspace.project01.actions.AbstractPage import AbstractPage
from com.workspace.project01.interfaces.LoginPage import LoginPage

class Login(AbstractPage, LoginPage):
    '''
    classdocs
    '''

    def enterUsername(self, username):
        self.enter(self.txtUsername, username)
    
    def enterPassword(self, password):
        self.enter(self.txtPassword, password)
    
    def login(self, username, password):
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLoginButton()
    
    def clickLoginButton(self):
        self.click(self.btnLogin)
    
    def checkErrorMessageDisplayed(self, message):
        messageContent = self.getElementText(self.lblErrorMessage)
        self.verifyTrue(messageContent == message, "The error message '%s' is displayed" % (message), 
                        "The error message '%s' is displayed instead of '%s'" % (messageContent, message))
    
    def checkUsernameTextboxDisplayed(self):
        isElementExist = self.doesElementDisplay(self.txtUsername)
        self.verifyTrue( isElementExist , "The username textbox is displayed",  "The username textbox is NOT displayed")
        
    def checkPasswordTextboxDisplayed(self):
        isElementExist = self.doesElementDisplay(self.txtPassword)
        self.verifyTrue( isElementExist , "The Password textbox is displayed",  "The Password textbox is NOT displayed")
    
    def checkLoginButtonDisplayed(self):
        isElementExist = self.doesElementDisplay(self.btnLogin)
        self.verifyTrue( isElementExist , "The Login button is displayed",  "The Login button is NOT displayed")
        
    def checkUsernameTextboxIsBlanked(self):
        elementText = self.getElementText(self.txtUsername)
        self.verifyTrue( elementText == "" , "The username textbox is blanked",  "The username textbox is NOT blanked")
        
    def checkPasswordTextboxIsBlanked(self):
        elementText = self.getElementText(self.txtPassword)
        self.verifyTrue( elementText == "" , "The Password textbox is blanked",  "The Password textbox is NOT blanked")
        
