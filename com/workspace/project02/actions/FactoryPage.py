# coding=utf-8
'''
Created on Aug 12, 2015

@author: phuong.dang
'''
from com.workspace.project01.actions.pages.Login import Login
from com.workspace.project01.actions.pages.General import General
from com.workspace.project01.actions.pages.ControlPanel import ControlPanel



class FactoryPage():
    '''
    classdocs
    '''

    @staticmethod
    def loginPage():
        return Login()
    
    @staticmethod
    def generalPage():
        return General()
    
    @staticmethod
    def controlPanelPage():
        return ControlPanel()