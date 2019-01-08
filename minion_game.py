"""
https://www.hackerrank.com/challenges/the-minion-game/problem
"""
vowels = 'AEIOU'
string = input("Enter the String:").upper()
stuart_consonents = 0
kevin_vowels = 0

for i in range(int(len(string))):
    if string[i] in vowels:
        kevin_vowels += len(string) - i
    else:
        stuart_consonents += len(string) - i

if kevin_vowels > stuart_consonents:
    print("Kevin %d" % kevin_vowels)
else:
    print("Stauart %d" % stuart_consonents)
