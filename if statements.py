#using "in" keyword
foods=['mushrooms','onions','pineapple']
if 'mushrooms' in foods:
    print("\n Mushrooms is in the list.")
if 'pepperon' not in foods:
    print("Pepperoni is not in the list.\n")    

#if-elif-else
age = 12
if age<14:
    price=0
elif age<18:
    price=25
else:
    price=40
print(f"Your bus ticket price is {price}rs.\n") 

#muliple condition
topping=['mushrooms','extra cheese']
if 'mushrooms' in topping:
    print("Adding mushrooms")
if 'pepperoni' in topping:
    print("Addind pepperoni")
if 'extra cheese' in topping:
    print("Adding extra cheese")
print("\n Finished making our pizza !")        



