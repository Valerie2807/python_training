from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


contactdate = [Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Belka",
                    title="Blabla", company="Romashka", address="Prospect Mira, 12",
                    home="789812878",
                    mobile="7879878777", work="78789787987", fax="87987897987",
                    email="jhggjhg@gmail.com",
                    email2="ffgh@mail.ru", email3="yggh@yandex.ru", homepage="www.google.com",
                    bday="4",
                    bmonth="May", byear="1992", aday="5", amonth="February", ayear="2017",
                    address2="Peshkov street", phone2="849943434", notes="QA")] + \
           [Contact(firstname=random_string("first_name", 10), lastname=random_string("last_name", 10),
                    middlename=random_string("middle_name", 10), company=random_string("company", 20),
                    address=random_string("address1", 20))
            for i in range(5)]


@pytest.mark.parametrize("contact", contactdate, ids=[repr(x) for x in contactdate])
def test_add_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Belka",
                               title="Blabla", company="Romashka", address="Prospect Mira, 12",
                               home="789812878",
                               mobile="7879878777", work="78789787987", fax="87987897987",
                               email="jhggjhg@gmail.com",
                               email2="ffgh@mail.ru", email3="yggh@yandex.ru", homepage="www.google.com",
                               bday="4",
                               bmonth="May", byear="1992", aday="5", amonth="February", ayear="2017",
                               address2="Peshkov street", phone2="849943434", notes="QA")
    app.contact.create(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
