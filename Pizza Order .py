
# Options and prices
pizza_choice = ["margarita", "pepperoni", "meat feast", "bbq chicken", "veggie"]

toppings_option = ["olives", "onions", "green pepper", "jalapenos"]

pizza_prices = {"margarita": 5, "pepperoni": 7, "meat feast": 6, "bbq chicken": 8, "vegetarian": 6.5}

topping_prices = {"olives" :1, "onions": 2, "green pepper": 3, "jalapenos": 4}
                  
sub_total = []
final_order = {}
customer_adress = {}

# for and while loop used to generate options
print("Hi, welcome to The  pizza shop!")
order_pizza = True
while order_pizza:    
    print("Please choose a pizza: ")
    print()
    for pizzas in pizza_choice:
        print(pizzas)
        print()
    while True:
        pizza = input("which pizza would you like to order? ")
        if pizza in pizza_choice:
            print(f"You have ordered a {pizza}.")
            sub_total.append(pizza_prices [pizza])
            break
        if pizza not in pizza_choice:
            print(f"I am sorry, we currently do not have {pizza}.")
# if the order topping is chosen you it will print chosen toppings elif no toppings added 
    order_topping = True
    print("This is the list of available extra toppings: ")
    for toppings in toppings_option:
        print(toppings)
        print()
    while order_topping:
        extra_topping = input("Would you like an extra topping? yes or no?")
        if extra_topping == "yes":
            topping = input("Which one would you like to add?")
            if topping in toppings_option:
                final_order.setdefault(pizza, [])
                final_order[pizza].append(topping)
                print(f"I have added {topping}.")
                sub_total.append(topping_prices[topping])
            else:
                print(f"I am sorry, we don't have {topping} available.")

        elif extra_topping == "no":
            break
    extra_pizza = input("Would you like to order another pizza?")
    if extra_pizza == "no":
        for key, value in final_order.items():
            print(f"\nYou have order a {key} pizza with {value}")
        check_order = True
        while check_order:
            print()
            order_correct = input("Is this correct? yes/no ")
            if order_correct == "yes":
                check_order = False
                order_pizza = False
            if order_correct == "no":
                print(final_order)
                add_remove = input("would you like to add or remove? ")
                if add_remove == "remove":
                    remove = input("Which pizza would you like to remove? ")
                    del final_order[remove]
                    print(final_order)
                if add_remove == "add":
                    check_order = False
# if correct user inputs provided the sub total will be calculated 
print(f"\nYour total order price is: £{sum(sub_total)}")

print("Please provide us with your name, adress and phonenumber")
customer_adress['name'] = input("what is your name?")
customer_adress['street_name'] = input("What is your streetname and housenumber?")
customer_adress['postalcode'] = input("What is the postalcode and cityname?")
customer_adress['phonenumber'] = input("What is your phonenumber?")
print()
print(f"Thank you for your order {customer_adress['name']}.")
print()
print("We will deliver your order to this adres ASAP")
print()
print(customer_adress['street_name'])
print(customer_adress['postalcode'])
print()
print(f"we will contact you on {customer_adress['phonenumber']} if anything comes up.")
