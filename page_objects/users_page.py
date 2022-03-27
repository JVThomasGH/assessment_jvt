from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class UsersPage:

    def __init__(self, driver):
        self.driver = driver

    _btn_add_user = (By.CSS_SELECTOR, "[type='add']")
    _input_first_name = (By.CSS_SELECTOR, "[name='FirstName']")
    _input_last_name = (By.CSS_SELECTOR, "[name='LastName']")
    _input_user_name = (By.CSS_SELECTOR, "[name='UserName']")
    _input_password = (By.CSS_SELECTOR, "[type='password']")
    _radio_company_aaa = (By.CSS_SELECTOR, "[value='15']")
    _radio_company_bbb = (By.CSS_SELECTOR, "[value='16']")
    _select_list_role = (By.XPATH, "//select[@name='RoleId']")
    _input_email = (By.CSS_SELECTOR, "[type='email']")
    _input_cellphone = (By.CSS_SELECTOR, "[name='Mobilephone']")
    _btn_save = (By.XPATH, "//button[@class='btn btn-success']")

    def btn_add_user(self):
        return self.driver.find_element(*UsersPage._btn_add_user)

    def input_first_name(self):
        self.driver.find_element(*UsersPage._input_first_name).clear()
        return self.driver.find_element(*UsersPage._input_first_name)

    def input_last_name(self):
        self.driver.find_element(*UsersPage._input_last_name).clear()
        return self.driver.find_element(*UsersPage._input_last_name)

    def input_user_name(self):
        self.driver.find_element(*UsersPage._input_user_name).clear()
        return self.driver.find_element(*UsersPage._input_user_name)

    def input_password(self):
        self.driver.find_element(*UsersPage._input_password).clear()
        return self.driver.find_element(*UsersPage._input_password)

    def radio_company_aaa(self):
        return self.driver.find_element(*UsersPage._radio_company_aaa)

    def radio_company_bbb(self):
        return self.driver.find_element(*UsersPage._radio_company_bbb)

    def select_list_role(self, item):
        select = Select(self.driver.find_element(*UsersPage._select_list_role))
        return select.select_by_visible_text(item)

    def input_email(self):
        self.driver.find_element(*UsersPage._input_email).clear()
        return self.driver.find_element(*UsersPage._input_email)

    def input_cellphone(self):
        self.driver.find_element(*UsersPage._input_cellphone).clear()
        return self.driver.find_element(*UsersPage._input_cellphone)

    def btn_save(self):
        return self.driver.find_element(*UsersPage._btn_save)
