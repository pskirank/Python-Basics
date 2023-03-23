def anti_vowel(text):
	t=""
	for i in text:
		for c in "aeiouAEIOU":
			if i==c:
				i=""
			else:
				i=i
		t=t+i
	return t
text2 = raw_input("Enter the String:")
print anti_vowel(text2)

"""
def anti_vowel(text):
    t=""
    for c in text:
        for i in "ieaouIEAOU":
            if c==i:
                c=""
            else:
                c=c
        t=t+c
    return t
"""