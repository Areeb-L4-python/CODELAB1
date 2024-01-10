sandwich_orders = ['chicken', 'cheese', 'beef']
finished_sandwiches = []

while sandwhich_orders:
    current_sandwich = sandwhich_orders.pop()
    print("Your"+ current_sandwich + "sandwich is being made.")
    finished_sandwiches.append(current_sandwich)

    print("\n")
    for sandwich is finished_sandwiches:
        print("your " + sandwich + "sandwich is ready.")