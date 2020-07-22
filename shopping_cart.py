num_of_items = int(input("Enter How many items did you buy?"))

sum = 0
for i in range(1, num_of_items):
	amount = int(input("What is the amount of the {} item".format(str(i))))
	sum += amount

print("The total price of all the items is {}$".format(sum))