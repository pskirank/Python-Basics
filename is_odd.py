def is_odd(x):
	while x > 0:
		if x % 2 == 0:
			return "Even"
			# print "Even"
		elif x % 2 == 1:
			return "Odd"
			# print "Odd"
x = input("Enter the Number:")
print("The given number is:", is_odd(x))
