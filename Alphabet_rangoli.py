"""
https://www.hackerrank.com/challenges/alphabet-rangoli/problem
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""
def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    array = []
    for i in range(n):
        s = "-".join(list(alphabet[i:n]))
        array.append(s[::-1]+s[1:])
    length = int(len(array[0]))
    array1 = [k.center(length, "-") for k in array[::-1]]
    val1 = "\n".join(array1)
    array2 = [j.center(length, "-") for j in array[1::]]
    val2 = "\n".join(array2)
    print(val1+"\n"+val2)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
