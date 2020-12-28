from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list', target_fixture="contact_list")
def contact_list(db):
    return db.get_contact_list()


@given('a contact', target_fixture="new_contact")
def new_contact():
    return (Contact("Fox", "J.", "Mulder", "Spooky", "Special Agent", "FBI", "Alexandria, Virginia",
                    "1(011)3456789", "+01190008432", "8-499-9576135", "No",
                    "spooky@fbi.com", "spookytest@fbi.com", "spookysuper@fbi.com",
                    "google.com", "13", "October", "1961", "13",
                    "October", "2021", "Ap. 42, 2630 Hegal Place",
                    "8 011 0002121", "The truth is out there"))


@when('I add the contact the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    assert len(new_contacts) == len(old_contacts) + 1
    old_contacts.append(new_contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)


@given('a non-empty contact list', target_fixture="non_empty_contact_list")
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact("Fox", "J.", "Mulder", "Spooky", "Special Agent", "FBI", "Alexandria, Virginia",
                    "1(011)3456789", "+01190008432", "8-499-9576135", "No",
                    "spooky@fbi.com", "spookytest@fbi.com", "spookysuper@fbi.com",
                    "google.com", "13", "October", "1961", "13",
                    "October", "2021", "Ap. 42, 2630 Hegal Place",
                    "8 011 0002121", "The truth is out there"))
    return db.get_contact_list()


@given('a random contact from the list', target_fixture="random_contact")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_delete(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.conact.get_conatact_list(),
                                                                     key=Contact.id_or_max)


@when('I edit the contact from the list')
def edit_contact(app, random_contact):
    app.contact.modify_contact_by_id(random_contact.id, random_contact)


@then('the new contact list is equal to the old list without the edit contact')
def verify_contact_delete(db, non_empty_contact_list, app, check_ui):
    old_contacts = non_empty_contact_list
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
