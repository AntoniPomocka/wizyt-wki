import sys
import logging
from faker import Faker
logging.basicConfig(level=logging.INFO)

class BaseContact:
   def __init__(self, name, surname, phone, email):
       self.name = name
       self.surname = surname
       self.phone = phone
       self.email = email
       self.label_length = len(name) + len(surname)


Dudek = BaseContact(name="Maciej", surname="Dudek", phone= "765876987", email="oqibz@example.com")

Gorski = BaseContact(name="Kacper", surname="Gorski", phone= "123345567", email="gorski@example.com")

Zieliński = BaseContact(name="Maurycy", surname="Zieliński", phone= "234432123", email="zielinski@example.com")
people = [Dudek, Gorski, Zieliński]


class BusinessContact(BaseContact):
  def __init__(self, position, company, workphone, *args, **kwargs ):
     super().__init__(*args, **kwargs)
     self.position = position
     self.company = company
     self.workphone = workphone

Adamski = BusinessContact(position="Manager", company="Apple", workphone="123123123", name= "Dawid", surname= "Adamski", phone= "898989752", email= "adamski@google.com" )

Kruszyński = BusinessContact(position="saler", company="Google", workphone="555675666", name= "Krzysztof", surname= "Kruszyński", phone= "26677381", email= "dzbanek@google.com" )

Woźniak = BusinessContact(position="Cleaner", company="Microsoft", workphone="873090123", name= "Barbara", surname= "Wożniak", phone= "653864123", email= "bezsensu@sen.pl")

logging.info("Do kogo chcesz zadzwonić: 1 Dudek, 2 Zieliński, 3 Gorski, 4 Adamski, 5 Kruszyński, 6 Woźniak:")
calling = input("wybierz osobę")
if calling == "1": 
   logging.info(f"Calling {Dudek.name} {Dudek.surname} at {Dudek.phone}")
elif calling == "2":
   logging.info(f"Calling {Zieliński.name} {Zieliński.surname} at {Zieliński.phone} ")
elif calling == "3":
   logging.info(f"Calling {Gorski.name} {Gorski.surname} at {Gorski.phone}")
elif calling =="4":
    number = input("Telefon prywatny czy służoby?")
    if number == "prywatny":
       logging.info(f"Calling {Adamski.name} {Adamski.surname} at {Adamski.phone}")
    else: logging.info(f"Calling {Adamski.name} {Adamski.surname} at {Adamski.workphone}")
elif calling == "5":
   number = input("Telefon prywatny czy służoby?")
   if number == "prywatny":
       logging.info(f"Calling {Kruszyński.name} {Kruszyński.surname} at {Kruszyński.phone}")
   else: logging.info(f"Calling {Kruszyński.name} {Kruszyński.surname} at {Kruszyński.workphone}")
elif calling == "6":
   number = input("Telefon prywatny czy służoby?")
   if number == "prywatny":
       logging.info(f"Calling {Woźniak.name} {Woźniak.surname} at {Woźniak.phone}")
   else: logging.info(f"Calling {Woźniak.name} {Woźniak.surname} at {Woźniak.workphone}")
                
else: logging.info("Nie ma takiej osoby")



fake = Faker()

class RandomContact:
    def __init__(self):
        self.name = fake.name()
        self.phone = fake.phone_number()
        self.email = fake.email()


random_contact = RandomContact()
print(f"Random Contact:")
print(f"Name: {random_contact.name}")
print(f"Phone: {random_contact.phone}")
print(f"Email: {random_contact.email}")