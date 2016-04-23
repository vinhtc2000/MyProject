'''
Created on Apr 20, 2016

@author: ZinhVcoin
'''
from com.workspace.project01.actions.FactoryPage import FactoryPage
from com.workspace.project01.actions.Common import Common
from com.workspace.project01.modules.Config import Config
import pytest
import os

class AbstractTest(FactoryPage, Config, Common):
    @pytest.fixture(scope = "function", autouse=True)
    def pre_condition_function(self, request):
        os.environ['PYTHON_TC_STATUS'] = "Passed"
        
        def post_condition_function():
            if (os.environ.get('PYTHON_TC_STATUS') == "Failed"):
                assert False
             
        request.addfinalizer(post_condition_function)