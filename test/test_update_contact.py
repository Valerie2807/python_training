from model.contact import Contact


def test_modify_contact_name_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="John", lastname="Doe",nickname="Belka",
                               title="Blabla", company="Romashka", address="Prospect Mira, 12",
                               home="789812878",
                               mobile="7879878777", work="78789787987", fax="87987897987",
                               email="jhggjhg@gmail.com",
                               email2="ffgh@mail.ru", email3="yggh@yandex.ru", homepage="www.google.com",
                               bday="4",
                               bmonth="May", byear="1992", aday="5", amonth="February", ayear="2017",
                               address2="Peshkov street", phone2="849943434", notes="QA"))
    old_contact = app.contact.get_contact_list()
    modify_contact = Contact(firstname="Elon", lastname="Mask", company="Google")
    modify_contact.id = old_contact[0].id
    app.contact.modify_first_contact(modify_contact)
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[0] = modify_contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


# def test_modify_contact_address(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="John", lastname="Doe",nickname="Belka",
#                                title="Blabla", company="Romashka", address="Prospect Mira, 12",
#                                home="789812878",
#                                mobile="7879878777", work="78789787987", fax="87987897987",
#                                email="jhggjhg@gmail.com",
#                                email2="ffgh@mail.ru", email3="yggh@yandex.ru", homepage="www.google.com",
#                                bday="4",
#                                bmonth="May", byear="1992", aday="5", amonth="February", ayear="2017",
#                                address2="Peshkov street", phone2="849943434", notes="QA"))
#     old_contact = app.contact.get_contact_list()
#     modify_contact_address = Contact(address="Wroclaw, Poland")
#     modify_contact_address.id = old_contact[0].id
#     app.contact.modify_first_contact(modify_contact_address)
#     assert len(old_contact) == app.contact.count()
#     new_contact = app.contact.get_contact_list()
#     old_contact[0] = modify_contact_address
#     assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
