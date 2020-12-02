from model.contact import Contact


def test_modify_contact_name_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="John", lastname="Doe"))
    old_contact = app.contact.get_contact_list()
    modify_contact = Contact(firstname="Elon", lastname="Mask", company="Google")
    modify_contact.id = old_contact[0].id
    app.contact.modify_first_contact(modify_contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = modify_contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


# def test_modify_contact_address(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="John", lastname="Doe"))
#     old_contact = app.contact.get_contact_list()
#     modify_contact_address = Contact(address="Wroclaw, Poland")
#     modify_contact_address.id = old_contact[0].id
#     app.contact.modify_first_contact(modify_contact_address)
#     new_contact = app.contact.get_contact_list()
#     assert len(old_contact) == len(new_contact)
#     old_contact[0] = modify_contact_address
#     assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
#
