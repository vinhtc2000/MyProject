'''
Created on Apr 23, 2016

@author: ZinhVcoin
'''
import os, sys, getopt
from time import gmtime, strftime
import imp

currentPath = os.path.dirname(os.path.realpath(__file__))
currentPath = currentPath.replace("\\", "/")
projectPath = currentPath + "/../../../../"

sys.path.append(projectPath) # Add project path to environment

if os.name == "nt": # Windows OS
    sys.path.append(";C:\Python27\Lib;C:\Python27\Scripts;C:\Python27\libs;C:\Python27\Lib\site-packages") # Import Python path
    
def doesLibIsImported(libName):
    try:
        imp.find_module(libName)
        return True
    except ImportError:
        return False
    
if doesLibIsImported("pytest") == False:
    if os.name == "nt": # Windows OS
        os.system("python -m pip install -U pytest==2.9.0") # Install pytest 2.9.0

if doesLibIsImported("allure") == False:
    if os.name == "nt": # Windows OS
        os.system("python -m pip install -U pytest_allure_adaptor==1.7.2") # Install pytest_allure_adaptor 2.9.0
    
if doesLibIsImported("selenium") == False:
    if os.name == "nt": # Windows OS
        os.system("python -m pip install -U selenium") # Install selenium

import pytest

def parseArgument(argv):
    tcs = ""
    feas = ""
    stos = ""
    sevs = ""
    
    try:
        opts, args = getopt.getopt(argv,"ht:f:s:sv",["testcases=","features=","stories=","severities="])
    except getopt.GetoptError:
        print 'RunTestSuite.py -t | testcases= <testcase01, testcase02,..>'
        print 'RunTestSuite.py -f | features= <feature01, feature02,..>'
        print 'RunTestSuite.py -s | stories= <story01, story02,..>'
        print 'RunTestSuite.py -se | severities= <blocker,critical,minor,normal,trivial>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'RunTestSuite.py -t | testcases= <testcase01, testcase02,..>'
            print 'RunTestSuite.py -f | features= <feature01, feature02,..>'
            print 'RunTestSuite.py -s | stories= <story01, story02,..>'
            print 'RunTestSuite.py -se | severities= <blocker,critical,minor,normal,trivial>'
            sys.exit()
        elif opt in ("-t", "--testcases"):
            tcs = arg
        elif opt in ("-f", "--features"):
            feas = arg
        elif opt in ("-s", "--stories"):
            stos = arg
        elif opt in ("-se", "--severities"):
            sevs = arg
    return tcs, feas, stos, sevs

def runTestSuite(tcNames, ftNames, stNames, svNames):
    ######################################## 
    # Create report path
    ########################################
    reportPath = "../reports/"
    d = os.path.dirname(reportPath)
    if not os.path.exists(d):
        os.makedirs(d)
           
    dateTime = strftime("%Y%m%d%H%M%S", gmtime())
    reportPath = '%sReport_%s/' % (reportPath, dateTime)
    d = os.path.dirname(reportPath)
    if not os.path.exists(d):
        os.makedirs(d)
    
    ########################################
    # Handle input data
    ########################################
    tcNames = str(tcNames).replace(" ", "")
    ftNames = str(ftNames).replace(" ", "")
    stNames = str(stNames).replace(" ", "")
    svNames = str(svNames).replace(" ", "")
    
    tcNames = str(tcNames).replace(",", " or ")
    
    ########################################
    # Convert data to generate commands
    ########################################
    tcCommand = ""
    ftCommand = ""
    stCommand = ""
    svCommand = ""
    
    # For test cases
    if tcNames != "":
        tcCommand = " -k \"%s\"" % (tcNames)
    
    # For features
    if ftNames != "":
        ftCommand = " --allure_features=%s" % (ftNames)
    
    # For stories
    if stNames != "":
        stCommand = " --allure_stories=%s" % (stNames)
    
    # For severities
    if svNames != "":
        svCommand = " --allure_severities=%s" % (svNames)
        
    pytestAllureCommand =  "-v -r aP --color=auto -x ../modules --alluredir %s %s %s %s %s" % (reportPath, tcCommand, ftCommand, stCommand, svCommand)
    
    ########################################
    # Running and collect results
    ########################################
    pytest.main(pytestAllureCommand) # Run test suite
    print "\"..\\..\\libs\\allure-commandline\\bin\\allure.bat\" generate %s -o %s/allure-report" %(reportPath, reportPath)
    os.system("\"..\\..\\libs\\allure-commandline\\bin\\allure.bat\" generate %s -o %s/allure-report" %(reportPath, reportPath)) # Generate report
    
if __name__ == "__main__":
    if sys.stdin.isatty(): # running from command line
        testCaseList, featuresList, storyList, severityList = parseArgument(sys.argv[1:]) # Get argument from command line
         
    else: # running from ide
        # Assign local variable
        testCaseList = ""
        featuresList = ""
        storyList = ""
        severityList = "" # blocker,critical,minor,normal,trivial
    
    runTestSuite(testCaseList, featuresList, storyList, severityList) # Call regression
