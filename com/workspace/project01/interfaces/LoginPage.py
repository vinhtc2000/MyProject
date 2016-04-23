'''
Created on Dec 1, 2015

@author: van.ngo
'''

class LoginPage():
    '''
    classdocs
    '''
    txtUsername = "//input[@id='mod-login-username']"
    txtPassword = "//input[@id='mod-login-password']"
    btnLogin = "//div[@class = 'button-holder']//a"
    lblErrorMessage = "//dd[@class='error message']//li"