def anticonsonent(text):
    t = ''
    for i in text:
        if i in 'aeiouAEIOU':
            i = i
        else:
            i = ''
        t += i
    return t.upper()

text1 = input("Enter the Text:")
print("Vowels in the given string are:", anticonsonent(text1))
