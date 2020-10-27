# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_contact(wd)
        self.go_to_contact_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def go_to_contact_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, wd):
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("hjhkh")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("hjkhh")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("jhjhk")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("jkhkjh")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("hjkhjhhj")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("hjkhjhh")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("hjkhjhkj")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("khjkh")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("7879878777")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("78789787987")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("87987897987")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("jhggjhg@gmail.com")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("ffgh@mail.ru")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("yggh@yandex.ru")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("www.google.com")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("4")
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("February")
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1992")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("4")
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("February")
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2017")
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("hjkhjh")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("hjkh")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("hkjhkj")
        wd.find_element_by_name("theform").click()
        # submit group creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")


    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
