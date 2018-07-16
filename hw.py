total = 0.0
# Loop continuously using while loop 
while True:	
    # Get the input using input.
    number = input("Enter number here :")
    # If the user press enter without put value 
    if number == '':
        # ...break the loop.
        break
    # Else try to add the number to the total.
    try:
        # This is the same as total = total + float(number)
        total = total + float(number)
	# But if input was not valid
    except ValueError: 
		# ...continue the loop.
        continue		
print("Total is", total)

