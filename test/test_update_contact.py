from model.contact import Contact


def test_modify_contact_name_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="John", lastname="Doe"))
    app.contact.modify_first_contact(Contact(firstname="Elon", lastname="Mask", company="Google"))


def test_modify_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="John", lastname="Doe"))
    app.contact.modify_first_contact(Contact(address="Wroclaw, Poland"))
