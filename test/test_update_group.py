import random
from model.group import Group
import allure
import pytest


def test_modify_group_name(app, db, check_ui, json_groups):
    group = json_groups
    with allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(group)
        old_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        group = random.choice(old_groups)
    with allure.step('When I edit the group from the list'):
        app.group.modify_group_by_id(group.id, group)
    with allure.step('Then the new group list is equal to the old list without the edit group'):
        assert len(old_groups) == app.group.count()
        new_groups = db.get_group_list()
        if check_ui:
            assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
