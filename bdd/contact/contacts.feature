Scenario Outline: Add new contact
  Given a contact list
  Given a contact
  When I add the contact the list
  Then the new contact list is equal to the old list with the added contact

Scenario Outline: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact

Scenario Outline: Edit a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I edit the contact from the list
  Then the new contact list is equal to the old list without the edit contact
