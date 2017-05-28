# coding=utf-8
'''
Created on Aug 12, 2015

@author: phuong.dang
'''
import os

class Config():
    # Set current path to environment
    os.environ['JOOMLA_PATH'] = (os.path.dirname(os.path.realpath(__file__)))
     
    cfSelectedLanguage = os.environ.get('SELECT_LANGUAGE',"US-CA-UK-DE")
    cfRanLanguage = os.environ.get('RAN_LANGUAGE','US')
    cfRunFullLanguages = os.environ.setdefault('RUN_FULL_LANGUAGES',"TRUE")
    cfDriver = os.environ.get('SELENIUM_DEVICE',"Firefox") #Firefox, Chrome, Ie
    cfCheckOrder = os.environ.get('CHECK_ORDER',"True")
    cfRequiredRun = os.environ.get('REQUIRED_RUN',"False")
    cfRequiredSite = os.environ.get('REQUIRED_SITE',"Staging")
    cfSikuliIDEPathFile = "C:\\Program Files (x86)\\Sikuli X\\Sikuli-IDE.bat"
    cfLongTimeWait = 180
    cfNormalTimeWait = 120
    cfShortTimeWait = 60
    cfImplicitlyTimeWait = 90
    cfPageLoadTimeout = 600
    cfShortTime = 20
    
    #
    cfJoomlaURL = "http://localhost/joomla25/administrator/"
    cfValidUsername = "admin"
    cfValidPassword = "admin"
    cfInvalidUsername = "invalidaccount"
    cfInvalidPassword = "invalidpassword"
        
        
    # Sauce Labs
    cfSauceLabsBROWSERS = os.environ.get('SAUCE_ONDEMAND_BROWSERS', None)
    cfSauceLabsUsername = os.environ.get('SAUCE_USERNAME', None)
    cfSauceLabsAccessKey = os.environ.get('SAUCE_ACCESS_KEY')
    cfSauceLabsUrl = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
    cfSauceLabsPlatform = os.environ.get('SELENIUM_PLATFORM')
    cfSauceLabsBrowserName = os.environ.get('SELENIUM_BROWSER')
    cfSauceLabsVersion = os.environ.get('SELENIUM_VERSION')
    cfSauceLabsBuild = str(os.environ.get('TEAMCITY_PROJECT_NAME')) + "_" + str(os.environ.get('TEAMCITY_BUILDCONF_NAME')) + str(os.environ.get('BUILD_NUMBER'))
    cfSauceLabsSeleniumDriver = os.environ.get('SELENIUM_DRIVER')
    cfSauceLabsSeleniumHost = os.environ.get('SELENIUM_HOST')
    cfSauceLabsSeleniumPort = os.environ.get('SELENIUM_PORT')
    cfSauceLabsIdleTimeout = 180
    cfSauceLabsMaxDuration = 3600
        
