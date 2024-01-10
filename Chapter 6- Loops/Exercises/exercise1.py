prompt="\nwhat topping would you like on your pizza?"
prompt+="\nenter 'quit' when you are finished"
while true:
    topping = input(prompt)
    while topping ='quit':
print("i will add"+ topping +"to your pizza.")
break
