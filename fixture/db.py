import pymysql

from model.contact import Contact
from model.group import Group


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.Connect(host=host,database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor =self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name,header=header,footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, address, home, "
                           "mobile, work, fax, email, email2, email3, homepage, address2, phone2,"
                           "notes from addressbook")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax,
                 email, email2, email3, homepage, address2, phone2, notes) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname,
                                       nickname=nickname, company=company, title=title, address=address,
                                       home=home, mobile=mobile, work=work, fax=fax, email=email,
                                       email2=email2, email3=email3, homepage=homepage, address2=address2,
                                       phone2=phone2, notes=notes))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
