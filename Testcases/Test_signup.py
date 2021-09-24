import pytest
from Testcases.BaseTest import BaseTest
from Pages.RegistrationPage import RegistrationPage

class Test_signUp(BaseTest):
    def test_dosignup(self):
        regPage=RegistrationPage(self.driver)
        regPage.fillform("abc","1234567","email@gmail.com","India","Pune","abc@1","qwerty")