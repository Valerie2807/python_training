import re

from model.contact import Contact


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == \
           merge_phones_like_on_home_page(contact_from_edit_page.home)
    # assert contact_from_home_page.work == clear(contact_from_edit_page.work)
    # assert contact_from_home_page.mobile == clear(contact_from_edit_page.mobile)
    # assert contact_from_home_page.phone2 == clear(contact_from_edit_page.phone2)


def test_phone_on_contact_view_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Fox", middlename="J.", lastname="Mulder", nickname="Spooky",
                                   title="Special Agent", company="FBI", address="Alexandria, Virginia",
                                   home="1(011)3456789", mobile="+01190008432", work="8-499-9576135", fax="No",
                                   email="spooky@fbi.com", email2="spookytest@fbi.com", email3="spookysuper@fbi.com",
                                   homepage="google.com", bday="13", bmonth="October", byear="1961", aday="13",
                                   amonth="October", ayear="2021", address2="Ap. 42, 2630 Hegal Place",
                                   phone2="8 011 0002121", notes="The truth is out there"))
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub('[() -]', "", s)

# 1- Склеиваем при помощи перевода строки, 2 - Отфильтровываем пустые строки, 3 - Удаляет все лишние символы,
# 4 - Отфильтровываются все пусты (None), 5 - Исходный список из 4 элементов
def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            (map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.home, contact.work, contact.mobile, contact.phone2])))))
