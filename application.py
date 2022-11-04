from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        wd = self.wd
        # открытие домашней страницы
        wd.get("http://localhost/addressbook")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        # авторизация
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self):
        wd = self.wd
        # открытие страницы групп
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # создание новой группы
        wd.find_element_by_name("new").click()
        # заполнение полей формы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # создание группы
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def create_contact(self, wdr, contact):
        wdr.find_element_by_link_text("add new").click()
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

    def return_to_groups_page(self):
        wd = self.wd
        # переход на страницу групп
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        # выход
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")

    def destroy(self):
        self.wd.quit()