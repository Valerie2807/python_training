import random
from model.group import Group


def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="Newtest"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    mod_group = Group(name="Newtest")
    app.group.modify_group_by_id(group.id, mod_group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="Newtest"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(name="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
