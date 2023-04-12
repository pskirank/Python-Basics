def reverse(text):
	word = ""
	l = len(text) - 1
	while l >= 0:
		word = word + text[l]
		l = l - 1
		return word
v = input("Enter the Text:")
reverse(v)
