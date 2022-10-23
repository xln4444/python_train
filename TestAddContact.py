# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wdr = webdriver.Firefox()
        self.wdr.implicitly_wait(30)

    def test_add_contact(self):
        wdr = self.wdr
        self.open_home_page(wdr)
        self.login(wdr)
        self.open_add_contact_page(wdr)
        self.create_contact(wdr)
        self.goto_home_page(wdr)

    def open_home_page(self, wdr):
        # открытие домашней страницы
        wdr.get("http://localhost/addressbook/edit.php")

    def login(self, wdr):
        # авторизация
        wdr.find_element_by_name("user").click()
        wdr.find_element_by_name("user").clear()
        wdr.find_element_by_name("user").send_keys("admin")
        wdr.find_element_by_name("pass").clear()
        wdr.find_element_by_name("pass").send_keys("secret")
        wdr.find_element_by_id("LoginForm").submit()

    def open_add_contact_page(self, wdr):
        # открытие страницы добавления нового контакта
        wdr.find_element_by_link_text("add new").click()

    def create_contact(self, wdr):
        # заполнение полей формы
        wdr.find_element_by_name("firstname").send_keys("First")
        wdr.find_element_by_name("middlename").send_keys("Middle")
        wdr.find_element_by_name("lastname").send_keys("Last")
        wdr.find_element_by_name("nickname").send_keys("Nick")
        wdr.find_element_by_name("title").send_keys("Zagolovok")
        wdr.find_element_by_name("company").send_keys("Company")
        wdr.find_element_by_name("address").send_keys("Address")
        wdr.find_element_by_name("home").send_keys("home")
        wdr.find_element_by_name("mobile").send_keys("Mobile")
        wdr.find_element_by_name("work").send_keys("Work")
        wdr.find_element_by_name("fax").send_keys("Fax")
        wdr.find_element_by_name("email").send_keys("e-mail1")
        wdr.find_element_by_name("email2").send_keys("e-mail2")
        wdr.find_element_by_name("email3").send_keys("e-mail3")
        wdr.find_element_by_name("homepage").send_keys("Homepage")
        wdr.find_element_by_name("bday").click()
        Select(wdr.find_element_by_name("bday")).select_by_visible_text("17")
        wdr.find_element_by_xpath("//option[@value='17']").click()
        wdr.find_element_by_name("bmonth").click()
        Select(wdr.find_element_by_name("bmonth")).select_by_visible_text("January")
        wdr.find_element_by_xpath("//option[@value='January']").click()
        wdr.find_element_by_name("byear").click()
        wdr.find_element_by_name("byear").clear()
        wdr.find_element_by_name("byear").send_keys("1993")
        wdr.find_element_by_name("aday").click()
        Select(wdr.find_element_by_name("aday")).select_by_visible_text("1")
        wdr.find_element_by_xpath("//div[@id='content']/form/select[3]/option[3]").click()
        wdr.find_element_by_name("amonth").click()
        Select(wdr.find_element_by_name("amonth")).select_by_visible_text("January")
        wdr.find_element_by_xpath("//div[@id='content']/form/select[4]/option[2]").click()
        wdr.find_element_by_name("ayear").click()
        wdr.find_element_by_name("ayear").clear()
        wdr.find_element_by_name("ayear").send_keys("2020")
        # заполнение блока дополнительной информации (Secondary)
        wdr.find_element_by_name("address2").click()
        wdr.find_element_by_name("address2").clear()
        wdr.find_element_by_name("address2").send_keys("Moscow")
        wdr.find_element_by_name("phone2").clear()
        wdr.find_element_by_name("phone2").send_keys("+79055405959")
        wdr.find_element_by_name("notes").clear()
        wdr.find_element_by_name("notes").send_keys("-")
        # создание контакта
        wdr.find_element_by_name("submit").click()

    def goto_home_page(self, wdr):
        # переход на домашнюю страницу
        wdr.find_element_by_link_text("home page").click()

    def is_element_present(self, how, what):
        try: self.wdr.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wdr.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wdr.quit()

if __name__ == "__main__":
    unittest.main()
