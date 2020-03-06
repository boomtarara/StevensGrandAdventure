from db_access import DBAccess

db = DBAccess()

characters_columns = db.fetch_column_names('characters')
items_columns = db.fetch_column_names('items')

db.insert_row('characters',('bob','1','2','3','inv','4'))
db.insert_row('characters',('rob','5','6','7','inv','8'))
db.insert_row('characters',('sob','9','10','11','inv','12'))


name = input("Who's stats do you want to see?" + str(db.fetch_names('characters')) + "\n")
choice = ''

while choice != 'x':
    choice = input(f"\n\n\nOptions for character {name}:\n"
          f"1) Change character choice\n"
          f"2) Show {name}'s stats\n"
          f"3) Update {name}'s stats\n"
          f"x) exit\n")
    if choice == '1':
        name = input("Who do you need want to switch to?:" + str(db.fetch_names('characters')) + "\n")
    elif choice == '2':
        print(db.fetch_row('characters',name))
    elif choice == '3':
        stat_name = input(f"What stat do you want to update? \n" + str(characters_columns) + "\n")
        stat_value = input("What is the new value? ")
        db.update_value('characters',name,stat_name,stat_value)
    else:
        print("\nDon't you play smart with me, son!\n")
