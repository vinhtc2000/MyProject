'''
Created on Dec 1, 2015

@author: van.ngo
'''

class NewArticlePage():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.txtTitle = "//ul[@class = 'adminformlist']//input[@class= 'inputbox required']"
        self.txtText = "html/body"
        
        self.btnToolbarBox = "//div[@id = 'toolbar']//a[normalize-space() = '$TOOLBAR BUTTON NAME$']"
        self.btnInsert = "//button[text() = 'Insert']"
        self.btnImage = "//a[text() = 'Image']"
        
        self.imgInsert = "//a[@title = '$IMAGE NAME$']"

        self.frmInsertAndUpload ="//div[@id = 'sbox-window']//iframe"
        self.frmImageForm = "//iframe[@name ='imageframe']"
        
        self.ddlStatus = "//select[@id='jform_state']/option[contains(.,'$STATUS ITEM$')]"
        self.ddlFeature = "//select[@id = 'jform_featured']"
        self.ddlCategory = "//select[@name='jform[catid]']"
        self.ddlAccess = "//select[@id = 'jform_access']"
               
        self.itmAccess = "//select[@id = 'jform_access']/option[contains(.,'$LEVEL ITEM$')]"
        self.itmCategory = "//select[@name='jform[catid]']/option[contains(.,'$ITEM NAME$')]"
        