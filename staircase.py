"""
print given number of steps using # symbols. If you simply print the number of #s, the stair case will come down developing in right side direction.
But you need to rpint the stair case developing down in left direction.
"""

rows = int(input("Enter the step count:"))

for i in range(1, rows+1):
    print(' '* (rows - i)+ '#' *i )
