from model.contact import Contact
import allure
import pytest


def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    with allure.step('Given a contact list'):
        old_contact = db.get_contact_list()
    with allure.step('When I add a user %s the list' % contact):
        app.contact.create(contact)
    with allure.step('Then the new user list is equal to the old list with the added user'):
        new_contact = db.get_contact_list()
        old_contact.append(contact)
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
