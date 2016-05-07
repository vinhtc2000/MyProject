# coding=utf-8
'''
Created on Aug 12, 2015

@author: phuong.dang
'''

from datetime import datetime, timedelta
from os.path import os
from time import gmtime, strftime
import time
import pytest
import imp

class Common():
    #####################################################################################
    # get current src path on local machine
    # Usage : getCurentSrcPath(argument_list)                                                              
    # Arguments list:                                                                                        
    #                                                                                                                  
    #     None
    #
    # Returns:
    #    Current src path
    #####################################################################################
    def getCurentSrcPath(self):
        # The current src path will be returned .../overdrive/
        return str(str(os.environ['JOOMLA_PATH']).replace("\\", "/")).split("overdrive/")[0] + "overdrive/"
    
    #####################################################################################
    # Print log with type is info
    # Usage : logInfo(argument_list)                                                              
    # Arguments list:                                                                                        
    #     log 
    # Returns:
    #    None
    #####################################################################################
    def logInfo(self, log):
        log = "[INFO]\t" + log
        with pytest.allure.step(log):  # @UndefinedVariable
            print self.getCurrentDateTime() + "\t" + log
        
        
    #####################################################################################
    # Print log with type is warning
    # Usage : logWarning(argument_list)                                                              
    # Arguments list:                                                                                        
    #     log 
    # Returns:
    #    None
    #####################################################################################
    def logWarning(self, log):
        # Calculate warnings number
        os.environ['JOOMLA_WARNINGS'] = str(int(os.environ['JOOMLA_WARNINGS']) + 1)
        
        log = self.getCurrentDateTime() + "\t[WARNING]\t" + log
        print log
    
    #####################################################################################
    # Print log with type is bug
    # Usage : logBug(argument_list)                                                              
    # Arguments list:                                                                                        
    #     log 
    # Returns:
    #    None
    #####################################################################################
    def logBug(self, log, number = 1):
        # Calculate warnings number
        for i in range(0, number):
            os.environ['JOOMLA_WARNINGS'] = str(int(os.environ['JOOMLA_WARNINGS']) + 1)
        
        log = self.getCurrentDateTime() + "\t[BUG]\t" + log
        print log
        
    #####################################################################################
    # Print log with type is fail
    # Usage : logFail(argument_list)                                                              
    # Arguments list:                                                                                        
    #     log 
    # Returns:
    #    None
    #####################################################################################
    def logFail(self, log, isSkip = False):
        if (isSkip == True):
            os.environ['PYTHON_TC_STATUS'] = "Failed"
        
        log = "[FAILED]\t " + log
        
        with pytest.allure.step(log):  # @UndefinedVariable
            print self.getCurrentDateTime() + "\t" + log
        
    #####################################################################################
    # Print log with type is pass
    # Usage : logPass(argument_list)                                                              
    # Arguments list:                                                                                        
    #     log 
    # Returns:
    #    None
    #####################################################################################
    def logPass(self, log):
        log = "[PASSED]\t" + log
        with pytest.allure.step(log):  # @UndefinedVariable
            print self.getCurrentDateTime() + "\t" + log
        
    #####################################################################################
    # Wait for xx seconds
    # Usage : wait(argument_list)                                                              
    # Arguments list:                                                                                                                                                                                                     
    #     seconds: the second time 
    # Returns:
    #    None
    #####################################################################################
    def wait(self, seconds):
        time.sleep(seconds)
    
    #####################################################################################
    # Generate a unique value type datetime 
    # Usage : generateUniqueValue(argument_list)                                                              
    # Arguments list:                                                                                                                                                                                                      
    #     None
    # Returns:
    #    Unique value string
    #####################################################################################
    def generateUniqueValue(self):
        return strftime("%Y%m%d%H%M%S", gmtime())
    
    #####################################################################################
    # Get current Date time 
    # Usage : getCurrentDateTime(argument_list)                                                              
    # Arguments list:                                                                                                                                                                                                      
    #     None
    # Returns:
    #    Current GM date time
    #####################################################################################
    def getCurrentDateTime(self):
        return strftime("%Y-%m-%d %H:%M:%S", gmtime())
    
    #####################################################################################
    # Get current Year
    # Usage : getCurrentYear(argument_list)                                                              
    # Arguments list:                                                                                                                                                                                                        
    #     None
    # Returns:
    #    Current GM Year
    #####################################################################################
    
    def getCurrentYear(self):
        return strftime("%Y", gmtime())
    
    def getCurrentMonth(self):
        return strftime("%m", gmtime())
    
    def getCurrentDay(self):
        return strftime("%d", gmtime())
    
    def getAbbreviatedMonthName(self):
        return strftime("%b", gmtime())
    
    def writeLogFile(self, logFilePath, value):
        try:
            pass
#             f = open(logFilePath, 'a+')
#             f.writelines(value + "\n")
#             f.close()
        except:
            pass
    #####################################################################################
    # Get EST time 
    # Usage : getESTTime(argument_list)                                                              
    # Arguments list:                                                                                                                                                                                                     
    #     None
    # Returns:
    #    Current EST time
    #####################################################################################
    def getESTTime(self, hoursValue = 0, minutesValue = 0, secondsValue = 0):
        return (datetime.utcnow() + timedelta(hours=-4 + hoursValue, minutes=minutesValue, seconds=secondsValue)).strftime("%m/%d/%Y %I:%M %p")
    
    def getPSTYear(self, hoursValue = 0, minutesValue = 0, secondsValue = 0):
        return (datetime.utcnow() + timedelta(hours=-7 + hoursValue, minutes=minutesValue, seconds=secondsValue)).strftime("%Y")
    
    def getPSTMonth(self, hoursValue = 0, minutesValue = 0, secondsValue = 0):
        return (datetime.utcnow() + timedelta(hours=-7 + hoursValue, minutes=minutesValue, seconds=secondsValue)).strftime("%b")
    
    def getGMTDate(self):
        return str(int(strftime("%d", gmtime())))
    
    def getPSTFullMonth(self, hoursValue = 0, minutesValue = 0, secondsValue = 0):
        return (datetime.utcnow() + timedelta(hours=-7 + hoursValue, minutes=minutesValue, seconds=secondsValue)).strftime("%B")
    
    def convertMoneyTypeToNumber(self, value, currency = "$"):
        num = value.replace(currency, "")
        num = str(num).replace(",", "")
        return float(num)
    
    def convertTimeValueToNumber(self, timeValue):
        if timeValue != None:
            minuteValue = str(timeValue).split(":")[0]
            secondValue = str(timeValue).split(":")[1]
            num = int(minuteValue) * 60 + int(secondValue)
        else:
            num = -1
        return num