shopping_list = []

while True:
    action = input("Would you like to [A]dd an item to the list, [R]emove an item from the list, [D]isplay the full list?, or [Q]uit program: ").uppercase
    if action == 'A':
        new_item = input("What item would you like to add?: ")
        shopping_list.append(new_item)
    if action == 'R':
        bad_item = input("What item would you like to remove: ")
        shopping_list.remove(bad_item)
    if action == 'D':
        print(shopping_list)
    if action == 'Q':
        break 
    else:
        print("Invalid Input")
