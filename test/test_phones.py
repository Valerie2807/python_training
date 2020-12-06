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
        app.contact.create(Contact(firstname="Victor", middlename="Joseph", lastname="Garber",
                                              nickname="Jack", title="Spy", company="CAI", address="Langley,Virginia",
                                              home="8(001)1230909", mobile="+01107000809",
                                              work="8-001-32161134", fax="-", email="jack.bristow@cia.com",
                                              email2="", email3="",homepage="", bday="12", bmonth="August", byear="1960",
                                              aday="26", amonth="October", ayear="2014", address2="Washington",
                                              phone2="8 011 7001222", notes="Alias"))
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub('[() -]', "", s)


# еще раз повторить как работает функция
def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            (map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.home, contact.work, contact.mobile, contact.phone2])))))
