from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number for contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    numbers = string.digits
    return "".join([random.choice(numbers) for i in range(random.randrange(maxlen))])


def random_email(maxlen):
    email = string.ascii_letters + string.digits
    return "".join([random.choice(email) for i in range(random.randrange(maxlen))]) + "@" + \
           "".join([random.choice(email) for i in range(random.randrange(maxlen))]) + ".com"


def random_symbols(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


contact_date = [Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Belka",
                    title="Blabla", company="Romashka", address="Prospect Mira, 12",
                    home="789812878",
                    mobile="7879878777", work="78789787987", fax="87987897987",
                    email="jhggjhg@gmail.com",
                    email2="ffgh@mail.ru", email3="yggh@yandex.ru", homepage="www.google.com",
                    bday="4",
                    bmonth="May", byear="1992", aday="5", amonth="February", ayear="2017",
                    address2="Peshkov street", phone2="849943434", notes="QA")] + \
           [Contact(firstname=random_string("first_name", 10), lastname=random_string("last_name", 10),
                    middlename=random_string("middle_name", 10), company=random_string("company", 20),
                    address=random_string("address1", 20))
            for i in range(5)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(contact_date))
