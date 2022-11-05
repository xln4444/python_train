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

    def create_contact(self, contact):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        # заполнение полей формы
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        #Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        #Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_xpath("//option[@value='January']").click()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        #Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        #Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[4]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[3]").click()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        # заполнение блока дополнительной информации (Secondary)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # создание контакта
        wd.find_element_by_name("submit").click()

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