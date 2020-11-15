from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Belka",
                               title="Blabla", company="Romashka", address="Prospect Mira, 12",
                               home="789812878",
                               mobile="7879878777", work="78789787987", fax="87987897987",
                               email="jhggjhg@gmail.com",
                               email2="ffgh@mail.ru", email3="yggh@yandex.ru", homepage="www.google.com",
                               bday="4",
                               bmonth="May", byear="1992", aday="5", amonth="February", ayear="2017",
                               address2="Peshkov street", phone2="849943434", notes="QA"))
    app.session.logout()

