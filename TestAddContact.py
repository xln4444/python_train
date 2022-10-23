# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from python_train.contact import Contact
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wdr = webdriver.Firefox()
        self.wdr.implicitly_wait(30)

    def test_add_contact(self):
        wdr = self.wdr
        self.open_home_page(wdr)
        self.login(wdr, username="admin", password="secret")
        self.open_add_contact_page(wdr)
        self.create_contact(wdr, Contact(firstname="First", middlename="Middle", lastname="Last", nickname="Nick", title="Title", company="Company", address="Address", home="+79010001100", mobile="+79010001101", work="+79010001102", fax="netu faxa", email="email@email.com", email2="email2@email.com", email3="email3@email.com", homepage="ya.ru", bday="1", bmonth="January", byear="1993", aday="2", amonth="February", ayear="1994", address2="Address2", phone2="phone2 495", notes="note note note"))
        self.goto_home_page(wdr)

    def open_home_page(self, wdr):
        # открытие домашней страницы
        wdr.get("http://localhost/addressbook/edit.php")

    def login(self, wdr, username, password):
        # авторизация
        wdr.find_element_by_name("user").send_keys(username)
        wdr.find_element_by_name("pass").send_keys(password)
        wdr.find_element_by_id("LoginForm").submit()

    def open_add_contact_page(self, wdr):
        # открытие страницы добавления нового контакта
        wdr.find_element_by_link_text("add new").click()

    def create_contact(self, wdr, contact):
        # заполнение полей формы
        wdr.find_element_by_name("firstname").send_keys(contact.firstname)
        wdr.find_element_by_name("middlename").send_keys(contact.middlename)
        wdr.find_element_by_name("lastname").send_keys(contact.lastname)
        wdr.find_element_by_name("nickname").send_keys(contact.nickname)
        wdr.find_element_by_name("title").send_keys(contact.title)
        wdr.find_element_by_name("company").send_keys(contact.company)
        wdr.find_element_by_name("address").send_keys(contact.address)
        wdr.find_element_by_name("home").send_keys(contact.home)
        wdr.find_element_by_name("mobile").send_keys(contact.mobile)
        wdr.find_element_by_name("work").send_keys(contact.work)
        wdr.find_element_by_name("fax").send_keys(contact.fax)
        wdr.find_element_by_name("email").send_keys(contact.email)
        wdr.find_element_by_name("email2").send_keys(contact.email2)
        wdr.find_element_by_name("email3").send_keys(contact.email3)
        wdr.find_element_by_name("homepage").send_keys(contact.homepage)
        Select(wdr.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        Select(wdr.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wdr.find_element_by_name("byear").send_keys(contact.byear)
        Select(wdr.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        Select(wdr.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wdr.find_element_by_name("ayear").send_keys(contact.ayear)
        # заполнение блока дополнительной информации (Secondary)
        wdr.find_element_by_name("address2").click()
        wdr.find_element_by_name("address2").clear()
        wdr.find_element_by_name("address2").send_keys(contact.address2)
        wdr.find_element_by_name("phone2").clear()
        wdr.find_element_by_name("phone2").send_keys(contact.phone2)
        wdr.find_element_by_name("notes").clear()
        wdr.find_element_by_name("notes").send_keys(contact.notes)
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
