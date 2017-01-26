import sqlite3
import User_Interface


# Create a table
def setup():
    try:
        db = sqlite3.connect('record_holder_db.db')  # Creates or opens database file
        cur = db.cursor()  # Need a cursor object to perform operations
        cur.execute('create table record_holder (Chainsaw_Juggling_Record_Holder text, Country text, Number_of_catches int)')

        try:
            db = sqlite3.connect('record_holder_db.db')  # Creates or opens database file
            cur = db.cursor()  # Need a cursor object to perform operations

            with db:
                cur.execute('insert into record_holder values ("Ian Stewart", "Canada", 94)')
                cur.execute('insert into record_holder values ("Aaron Gregg", "Canada", 88)')
                cur.execute('insert into record_holder values ("Chad Taylor", "USA", 78)')

                # db.commit()  # Don't need - will be called automatically by the context manager if there's no error.
        except sqlite3.Error as e:
            print('Error adding rows')
            print(e)
            # In the event of an error, transactions will be automatically rolled back.

    except sqlite3.Error:
        print()

    finally:
        db.close()

def handle_choice(choice):

    if choice == '1':
        insert_row()

    elif choice == '2':
        view_records()

    elif choice == '3':
        delete_row()

    elif choice == '4':
        search_records()

    elif choice == '5':
        update_catches()

    elif choice == 'q':
        quit()

    else:
        print('Please enter a valid selection')

def delete_row():
    try:
        db = sqlite3.connect('record_holder_db.db')  # Creates or opens database file
        cur = db.cursor()  # Need a cursor object to perform operations
        record_delete = input('Please enter the name of the record holder to delete:')

        cur.execute('DELETE FROM record_holder WHERE Chainsaw_Juggling_Record_Holder = (?)', (record_delete,))
        db.commit()
    except sqlite3.Error as e:
        print('Error deleting the record holder from record_holder table')
        print(e)

    finally:
        db.close()

def update_catches():
    try:
        db = sqlite3.connect('record_holder_db.db')  # Creates or opens database file
        cur = db.cursor()  # Need a cursor object to perform operations
        record_name = input('Please enter the name of the record holder to update:')
        record_catches = input('Please enter the amount of catches you want to update:')
        cur.execute('UPDATE record_holder SET Number_of_catches = (?) WHERE Chainsaw_Juggling_Record_Holder = (?)', (record_catches, record_name,))
        db.commit()
    except sqlite3.Error as e:
        print('Error deleting the record holder from record_holder table')
        print(e)

    finally:
        db.close()

def view_records():
    # Execute a query. Do not need a context manager, as no changes are being made to the DB
    try:
        db = sqlite3.connect('record_holder_db.db')  # Creates or opens database file
        cur = db.cursor()  # Need a cursor object to perform operations

        for row in cur.execute('select * from record_holder'):
            print(row)

    except sqlite3.Error as e:
        print('Error selecting data from record_holder table')
        print(e)

    finally:
        db.close()

def search_records():
    # Execute a query. Do not need a context manager, as no changes are being made to the DB
    try:
        db = sqlite3.connect('record_holder_db.db')  # Creates or opens database file
        cur = db.cursor()  # Need a cursor object to perform operations

        record_search = input('Please enter the name of the record holder you want to search for:')

        for row in cur.execute('select * from record_holder WHERE Chainsaw_Juggling_Record_Holder = (?)', (record_search,)):
            print(row)

    except sqlite3.Error as e:
        print('Error selecting data from record_holder table')
        print(e)

    finally:
        db.close()

def insert_row():
    db = sqlite3.connect('record_holder_db.db')  # Creates or opens database file

    cur = db.cursor()  # Need a cursor object to perform operations

    # Create a table if not exists...
    cur.execute('create table if not exists record_holder (Chainsaw_Juggling_Record_Holder text, Country text, Number_of_catches int)')

    # Ask user for information for a new phone
    name = input('Enter name of record holder: ')
    country = input('Enter the Country of the record holder: ')
    number_catches = int(input('Enter the number of catches (as an integer): '))

    # Parameters. Use a ? as a placeholder for data that will be filled in
    # Provide data as a second argument to .execute, as a tuple of values
    cur.execute('insert into record_holder values (?, ?, ?)', (name, country, number_catches))

    # Fetch and display all data. Results stored in the cursor object
    cur.execute('select * from record_holder')

    for row in cur:
        print(row)

    db.commit()  # Ask the database to save changes!


def main():

    setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = User_Interface.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
