from model.contact import Contact


def test_modify_contact_name_company(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Elon", lastname="Mask", company="Google"))
    app.session.logout()


def test_modify_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(address="Wroclaw, Poland"))
    app.session.logout()
