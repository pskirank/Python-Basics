# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
def likes(names):
    if len(names) == 0:
        return "No one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s , %s and %s like this" % (names[0], names[1], names[2])
    else:
        k = len(names) - 2
        return "%s, %s and %s others like this" % (names[0], names[1], k)
array1 = []
array2 = ['Kevin', 'Ramesh', 'Hari', 'Peter']
print (likes(array2))