import random
import allure
from model.contact import Contact


def test_modify_contact_name_company(app, db, check_ui, json_contacts):
    contact = json_contacts
    with allure.step('Given a non-empty contact list'):
        if len(db.get_contact_list()) == 0:
            app.user.create(contact)
        old_contact = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact = random.choice(old_contact)
    with allure.step('When I edit the contact from the list'):
        app.contact.modify_contact_by_id(contact.id, contact)
    with allure.step('Then the new contact list is equal to the old list without the edit contact'):
        assert len(old_contact) == app.contact.count()
        new_contact = db.get_contact_list()
        assert len(old_contact) == len(new_contact)
        if check_ui:
            assert sorted(old_contact, key=Contact.id_or_max) == \
                   sorted(app.group.get_group_list(), key=Contact.id_or_max)
