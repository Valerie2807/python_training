import random
import allure
from model.contact import Contact


def test_delete_some_contact(app, db, check_ui, json_contacts):
    contact = json_contacts
    with allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
            app.contact.create(contact)
        old_contact = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact = random.choice(old_contact)
    with allure.step('When I delete the contact from the list'):
        app.contact.delete_contact_by_id(contact.id)
    with allure.step('Then the new contact list is equal to the old list without the deleted contact'):
        assert len(old_contact) - 1 == app.contact.count()
        new_contact = db.get_contact_list()
        old_contact.remove(contact)
        assert sorted(new_contact, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
