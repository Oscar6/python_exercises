# Phone Book App

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
    elif choice==2:
        print("Set an entry: ")