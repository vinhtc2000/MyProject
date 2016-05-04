'''
Created on Dec 1, 2015

@author: van.ngo
'''

class ManagerArticlePage():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.btnToolBar = "//div[@id ='toolbar']//a[contains(., '$BUTTON NAME$')]"
        self.btnSearch = "//div[@class='filter-search fltlft']//button[text() = 'Search']"
        
        self.lblMessage =  "//div[@id='system-message-container']//li[contains(., '$MESSAGE$')]"
        
        self.tblArticle = "//table[@class= 'adminlist']/tbody"
        self.celArticle = "//table[@class= 'adminlist']//td[descendant::a[contains(.,'$ARTICLE$')]]"
        self.colProperty ="//table[@class = 'adminlist']//th[descendant::a[text() = '$PROPERTY$']]"
        self.celPropertyValue = "//tr[descendant::a[contains(.,'$ARTICLE$')]]/td[$INDEX$]"
        
        self.txtSearch = "//div[@class='filter-search fltlft']//input[@id = 'filter_search']"
        self.txtStatus = "//tr[descendant::a[contains(.,'$ARTICLE$')]]//span[@class = 'text']"

        self.chkArticle = "//tr[descendant::a[contains(.,'$ARTICLE$')]]//input[@type = 'checkbox']"
        
        self.ddlStatus = "//select[@name = 'filter_published']/option[contains(.,'$ITEM NAME$')]"
        self.ddlDisplay = "//select[@id = 'limit']//option[text() = '$NUMBER OF ARTICLE$']"
        
        self.barPage ="//div[@class = 'pagination']//div[@class = 'page']"

        self.icnStatus = "//tr[descendant::a[contains(.,'$ARTICLE$')]]//a[@class = 'jgrid hasTip']"

        self.imgFeaturedToggle = "//tr[descendant::a[contains(.,'$ARTICLE$')]]//img"
