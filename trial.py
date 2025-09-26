#Use of if statements with a for loop
req_toppings=['mushrooms','green pepper','extra cheese']
for req_topping in req_toppings:
    if req_topping=='green pepper':
        print("Sorry,we are out of green peppers right now.")
    else: 
        print(f"Adding {req_topping}.")
        print(f"\n Finish making your pizza !")

#Using multiple lists
available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings: 
        print(f"Adding {requested_topping}.")
    else:
        print(f"sorry,we dont have {requested_topping}.")
        print("\n Finish making your pizza!")
