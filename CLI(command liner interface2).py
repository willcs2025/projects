import argparse
import sqlite3


class People:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __repr__(self):
        return f"People('{self.name}', {self.number})"


# Conexão com o banco de dados
conn = sqlite3.connect("contacts.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS contacts(name TEXT UNIQUE, number INTEGER)")


def add_contact(people):
    with conn:
        c.execute("INSERT INTO contacts VALUES(?,?)", (people.name, people.number))


def search_contact(name):
    c.execute("SELECT * FROM contacts WHERE name=?", (name,))
    return c.fetchall()


def remove_contact(people):
    with conn:
        c.execute("DELETE FROM contacts WHERE name=? AND number=?", (people.name, people.number))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Contacts",
        usage="use -h or --help",
        description="""
        ------------------------------
        DESCRIPTION:
        A tool for adding, searching or 
        deleting a contact
        ------------------------------
        """,
        epilog="copyright @ pranav",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        add_help=True
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--show", "-s", help="Option for searching a contact", action="store_true")
    group.add_argument("--add", "-a", help="Option for adding a contact", action="store_true")
    group.add_argument("--delete", "-d", help="Option for deleting a contact", action="store_true")
    
    parser.add_argument("--name", "-n", help="Name of the contact", action="store", type=str)
    parser.add_argument("--number", "-no", help="Number of the contact", action="store", type=int)

    arg = parser.parse_args()

    # Lógica dos Comandos
    if arg.add:
        name = arg.name
        num = arg.number
        if name and num:
            people = People(name, num)
            try:
                add_contact(people)
                print("Contact added successfully")
            except sqlite3.IntegrityError:
                print("Error: A contact with this name already exists.")
        else:
            print("Please provide both name and number to add a contact.")

    elif arg.show:
        name = arg.name
        if name:
            contact = search_contact(name)
            if len(contact) > 0:
                print(f"Name: {contact[0][0]}, Number: {contact[0][1]}")
            else:
                print("There are no contacts with that name.")
        else:
            print("Please provide a name to search.")

    elif arg.delete:
        name = arg.name
        num = arg.number
        if name and num:
            contact = search_contact(name)
            if len(contact) > 0:
                people = People(name, num)
                remove_contact(people)
                print("Contact deleted successfully")
            else:
                print("There are no contacts with that name.")
        else:
            print("Please provide both name and number to delete the contact.")
        









        
