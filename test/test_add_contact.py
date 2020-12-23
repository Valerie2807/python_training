from model.contact import Contact


def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    old_contact = db.get_contact_list()
    app.contact.create(contact)
    new_contact = db.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
