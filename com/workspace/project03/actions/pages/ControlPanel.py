'''
Created on Apr 15, 2016

@author: ZinhVcoin
'''
from com.workspace.project01.actions.AbstractPage import AbstractPage
from com.workspace.project01.interfaces.ControlPanelPage import ControlPanelPage

class ControlPanel(AbstractPage, ControlPanelPage):
    '''
    classdocs
    '''
    
    def checkPageIsDisplayed(self):
        self.verifyTrue(self.doesElementExisted(self.pagUnique), "The Control Panel page is displayed", 
                        "The Control Panel page isn't displayed")