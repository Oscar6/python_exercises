# Phone Book App

phonebook_dict = { 
    #contact[0]
        'Oscar': '703-493-1834', 
        'Olive': '857-384-1234', 
        'Mars': '484-584-2923'
    }

def print_menu():       ## Your menu design here
    print(25 * "=", "Phone Book App", 25 * "=")
    print("1. Look up an entry")
    print("2. Set an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Quit")

loop=True

while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("What do you want to do? Select [1-5]: ")
     
    if choice==1:     
        print("Look up an entry. Please enter name: ")
        ## You can add your code or functions here
        if choice == 'Oscar':
            nameContact = phonebook_dict[0]['Oscar']
            print(nameContact)

    elif choice==2:
        print("Set an entry: ")
    
    elif choice==3:
        print("Delete an entry: ")

    elif choice==4:
        print("List all entries: ")
    
    elif choice==5:
        print("Quit")
        loop = False
        break
    else:
        if 6 <= int(choice) <= 100:
            input('Please choose an option between 1-5:')
            
