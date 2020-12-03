from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and
                len(wd.find_elements(By.XPATH, "//form[2]/div[1]/input")) > 0):
            wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_home_page()
        self.contact_cashe = None

    def select_day(self, add_day, number):
        wd = self.app.wd
        if number is not None:
            Select(wd.find_element(By.NAME, add_day)).select_by_visible_text(number)
            wd.find_element(By.NAME, add_day).click()

    def select_month(self, add_month, month):
        wd = self.app.wd
        if month is not None:
            Select(wd.find_element(By.NAME, add_month)).select_by_visible_text(month)
            wd.find_element(By.NAME, add_month).click()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.select_day("bday", contact.bday)
        self.select_month("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.select_day("aday", contact.aday)
        self.select_month("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, filed_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(filed_name).click()
            wd.find_element_by_name(filed_name).clear()
            wd.find_element_by_name(filed_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element(By.CSS_SELECTOR, "div.msgbox")
        self.contact_cashe = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        wd.find_element(By.XPATH, "//tbody/tr[2]/td[8]/a").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cashe = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cashe = None

    def get_contact_list(self):
        if self.contact_cashe is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cashe = []
            for elements in wd.find_elements(By.NAME, "entry"):
                element = elements.find_elements(By.TAG_NAME, "td")
                id = elements.find_element(By.NAME, "selected[]").get_attribute("value")
                last_text = element[1].text
                first_text = element[2].text
                address = element[3].text
                self.contact_cashe.append(Contact(lastname=last_text, firstname=first_text, id=id, address=address))
        return list(self.contact_cashe)
