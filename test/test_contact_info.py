from model.contact import Contact
from random import randrange
import re


def test_check_contact_info_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Fox", middlename="J.", lastname="Mulder", nickname="Spooky",
                                   title="Special Agent", company="FBI", address="Alexandria, Virginia",
                                   home="1(011)3456789", mobile="+01190008432", work="8-499-9576135", fax="No",
                                   email="spooky@fbi.com", email2="spookytest@fbi.com", email3="spookysuper@fbi.com",
                                   homepage="google.com", bday="13", bmonth="October", byear="1961", aday="13",
                                   amonth="October", ayear="2021", address2="Ap. 42, 2630 Hegal Place",
                                   phone2="8 011 0002121", notes="The truth is out there"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub('[() -]', "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.home, contact.mobile,
                                                                 contact.work, contact.phone2]))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
