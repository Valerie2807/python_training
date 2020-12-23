from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_group(app, orm):
    if len(app.contact.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="Eugene", lastname="Pak"))
    if len(app.group.get_group_list()) == 0:
        app.group.create(Group(name="namename", header="headerheader"))
    all_groups = orm.get_group_list()
    all_contacts = orm.get_contact_list()
    contact = random.choice(all_contacts)
    group_with_contact = orm.get_groups_containing_contact(contact)
    if len(group_with_contact) == 0:
        group = random.choice(all_groups)
        app.contact.add_contact_to_group_by_id(contact.id, group.id, group.name)
        group_with_contact = orm.get_groups_containing_contact(contact)
    group = random.choice(group_with_contact)
    app.contact.delete_contact_from_group(group.id, contact.id)
    contacts_not_in_group = orm.get_contacts_not_in_group(group)
    assert contact in contacts_not_in_group
