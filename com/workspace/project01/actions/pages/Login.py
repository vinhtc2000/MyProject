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