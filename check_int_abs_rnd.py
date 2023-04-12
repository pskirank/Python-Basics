x = input("Enter the Number (non-integer):")
print("Rounded value of this number is:", round(x))
print("Absolute value of this number is:", abs(x))

def is_int(x):
  y = abs(x)
  z = round(x)
  if y - z == 0:
    return "Integer"
  else:
    return "Non Integer"
k = input("Enter the number:")
print("Lets check the integer'ship of this number:",is_int(k))