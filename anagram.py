def anagram_find(word1, word2):
    #word1 = sorted(word1.replace(' ','').lower())
    word1 = sorted(list(word1.lower()))
    #word2 = sorted(word2.replace(' ','').lower())
    word2 = sorted(list(word2.lower()))
    return word1 == word2
print(anagram_find('Heart all', 'Earth lal'))
