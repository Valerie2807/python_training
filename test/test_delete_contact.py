from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="John", lastname="Doe", nickname="Belka",
                               title="Blabla", company="Romashka", address="Prospect Mira, 12",
                               home="789812878",
                               mobile="7879878777", work="78789787987", fax="87987897987",
                               email="jhggjhg@gmail.com",
                               email2="ffgh@mail.ru", email3="yggh@yandex.ru", homepage="www.google.com",
                               bday="4",
                               bmonth="May", byear="1992", aday="5", amonth="February", ayear="2017",
                               address2="Peshkov street", phone2="849943434", notes="QA"))
    old_contact = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contact) - 1 == app.group.count()
    new_contact = app.contact.get_contact_list()
    old_contact[0:1] = []
    assert old_contact == new_contact
