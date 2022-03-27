
from time import sleep

from assertpy import assert_that
from selenium.webdriver.common.by import By

from page_objects.users_page import UsersPage
from utilities.base_class import BaseClass


class TestWeb(BaseClass):
    def test_web_table(self, data_set, setup):
        log = self.get_logger()
        users_page = UsersPage(self.driver)
        title = self.driver.title
        log.info(title)
        assert_that(title).contains("WebTables")
        log.info(f"Successfully opened {title}")

        users_page.btn_add_user().click()
        users_page.input_first_name().send_keys(data_set["first_name"])
        users_page.input_last_name().send_keys(data_set["last_name"])
        users_page.input_user_name().send_keys(data_set["user_name"])
        users_page.input_password().send_keys(data_set["password"])
        if data_set["customer"] == "CompanyAAA":
            users_page.radio_company_aaa().click()
        elif data_set["customer"] == "CompanyBBB":
            users_page.radio_company_bbb().click()
        users_page.select_list_role(data_set["role"])
        users_page.input_email().send_keys(data_set["email"])
        users_page.input_cellphone().send_keys(data_set["cell"])
        users_page.btn_save().click()
        tabel_rows = self.driver.find_elements(By.XPATH, "//tbody/tr")
        user = data_set["user_name"]
        for row in tabel_rows:
            if user in row.text:
                assert True, f"Table contains {user}"
                break
            else:
                assert False, f"Table does NOT contain {user}"
        sleep(1)
