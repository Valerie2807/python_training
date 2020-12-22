# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, json_groups):
  group = json_groups
  old_groups = app.group.get_group_list()
  group = Group(name="TestGroup", header="header", footer="footer")
  app.group.create(group)
  new_groups = app.group.get_group_list()
  old_groups.append(group)
  assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


