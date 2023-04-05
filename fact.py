def fact(x):
	temp = 1
	x = int(x)
	while x > 0 :
		temp=temp * x

		x=x-1
		print x
	return temp

