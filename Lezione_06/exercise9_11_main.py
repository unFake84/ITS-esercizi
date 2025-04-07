'''
Imported Admin:

1.
    Create a module users.py containing three classes:

    1a.
        User: stores first_name, last_name, username, and email;
        includes describe_user() and greet_user() methods.

    1b.
        Privileges: holds a list of privileges and a method show_privileges() to display them.

    1c.
        Admin: stores a User instance and a Privileges instance as attributes.
        
2.
    In a separate file main.py, import the classes,
    create a User and a Privileges instance, pass them to Admin,
    and call describe_user() and show_privileges() to verify everything works correctly.

'''

#2.
from exercise9_11_users import *

panco: User = User("Pinco", "Panco", "PancoPinco", "PeP@punco.poc")
privilegio_panco: Privileges = Privileges("amministatore")

admin_panco = Admin(panco, privilegio_panco)

print(panco.describe_user())
admin_panco.privilegi.show_privileges()