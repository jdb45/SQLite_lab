import sqlite3
import User_Interface


# Create a table
def setup():
    try:
        # Creates or opens the database file
        db = sqlite3.connect('record_holder_db.db')
        cur = db.cursor()
        # creating the table
        cur.execute('create table record_holder (Chainsaw_Juggling_Record_Holder text, Country text, Number_of_catches int)')

        try:
            # I was not sure if I needed this. I will test when I have more time
            db = sqlite3.connect('record_holder_db.db')
            cur = db.cursor()

            with db:
                #adding records to the table
                cur.execute('insert into record_holder values ("Ian Stewart", "Canada", 94)')
                cur.execute('insert into record_holder values ("Aaron Gregg", "Canada", 88)')
                cur.execute('insert into record_holder values ("Chad Taylor", "USA", 78)')

        except sqlite3.Error as e:
            print('Error adding rows')
            print(e)

    except sqlite3.Error:
        print()

    finally:
        db.close()

def handle_choice(choice):
    #handler menu
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
        db = sqlite3.connect('record_holder_db.db')
        cur = db.cursor()
        #getting the input from the user
        record_delete = input('Please enter the name of the record holder to delete:')
        # deleting a record
        cur.execute('DELETE FROM record_holder WHERE Chainsaw_Juggling_Record_Holder = (?)', (record_delete,))
        db.commit()
    except sqlite3.Error as e:
        print('Error deleting the record holder from record_holder table')
        print(e)

    finally:
        db.close()

def update_catches():
    try:
        db = sqlite3.connect('record_holder_db.db')
        cur = db.cursor()
        # getting the information to update the record
        record_name = input('Please enter the name of the record holder to update:')
        record_catches = input('Please enter the amount of catches you want to update:')
        #updating the catches for the record holder
        cur.execute('UPDATE record_holder SET Number_of_catches = (?) WHERE Chainsaw_Juggling_Record_Holder = (?)', (record_catches, record_name,))
        db.commit()
    except sqlite3.Error as e:
        print('Error deleting the record holder from record_holder table')
        print(e)

    finally:
        db.close()

def view_records():
    #view all recoreds in the DB
    try:
        db = sqlite3.connect('record_holder_db.db')
        cur = db.cursor()

        for row in cur.execute('select * from record_holder'):
            print(row)

    except sqlite3.Error as e:
        print('Error selecting data from record_holder table')
        print(e)

    finally:
        db.close()

def search_records():

    try:
        db = sqlite3.connect('record_holder_db.db')
        cur = db.cursor()
        #getting input to search for a record
        record_search = input('Please enter the name of the record holder you want to search for:')

        for row in cur.execute('select * from record_holder WHERE Chainsaw_Juggling_Record_Holder = (?)', (record_search,)):
            print(row)

    except sqlite3.Error as e:
        print('Error selecting data from record_holder table')
        print(e)

    finally:
        db.close()

def insert_row():
    db = sqlite3.connect('record_holder_db.db')

    cur = db.cursor()

    cur.execute('create table if not exists record_holder (Chainsaw_Juggling_Record_Holder text, Country text, Number_of_catches int)')

    # Ask user for information for the record holder
    name = input('Enter name of record holder: ')
    country = input('Enter the Country of the record holder: ')
    number_catches = int(input('Enter the number of catches (as an integer): '))

    # inserting the new data into the table
    cur.execute('insert into record_holder values (?, ?, ?)', (name, country, number_catches))

    cur.execute('select * from record_holder')

    for row in cur:
        print(row)

    db.commit()  


def main():

    setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = User_Interface.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
