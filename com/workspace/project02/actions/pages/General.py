'''
Created on Apr 20, 2016

@author: ZinhVcoin
'''
from com.workspace.project01.actions.AbstractPage import AbstractPage
from com.workspace.project01.interfaces.GeneralPage import GeneralPage

class General(AbstractPage, GeneralPage):
    '''
    classdocs
    '''

    def logOut(self, username):
        self.click(self.lnkLogOut)
