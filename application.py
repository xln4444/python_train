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

    def return_to_groups_page(self):
        wd = self.wd
        # переход на страницу групп
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        # выход
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()