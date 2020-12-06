from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and
                len(wd.find_elements(By.XPATH, "//form[2]/div[1]/input")) > 0):
            wd.find_element_by_link_text("home").click()

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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        # wd.switch_to_alert().accept()
        alert = wd.switch_to.alert
        alert.accept()
        wd.find_element(By.CSS_SELECTOR, "div.msgbox")
        self.open_home_page()
        self.contact_cashe = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.select_contact_by_index(index)
        choose_contact = wd.find_elements_by_name("entry")[index]
        element = choose_contact.find_elements_by_tag_name("td")[7]
        element.find_element_by_tag_name("a").click()
        # wd.find_element(By.XPATH, "//tbody/tr[2]/td[8]/a").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cashe = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cashe = None
    # Кеширование списка контактов, сбрасывается после добавления\удаления\модификации

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
                all_phones = element[5].text
                self.contact_cashe.append(Contact(lastname=last_text, firstname=first_text,
                                                  all_phones_from_home_page=all_phones, id=id, address=address))
        return list(self.contact_cashe)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home=home, work=work, mobile=mobile, phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)

