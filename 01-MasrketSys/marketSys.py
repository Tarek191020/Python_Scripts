shopping_List = []

print ("Supermarket System")
while True:
    print("Hello\n1. add items\n2. delete item\n3. display items\n4. clear list\n5. exit program")
    choice = int (input("choose what you want:\n"))
    
    if choice == 1:
        shopping_List.append(input("Enter item to add:\n"))
    elif choice == 2:
        shopping_List.remove(input("Enter item to delete:\n"))
    elif choice == 3:
        print("Shopping List is : ",shopping_List)
    elif choice == 4:
        shopping_List.clear()
    elif choice == 5:
        print("Program exititg done\n")
        break
    else:
        print("Invalid choice, Enter number again:\n")
