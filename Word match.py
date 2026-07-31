def word_match(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("List of words with first and last characters are: \n", lst)
    return ctr

count = word_match(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("Number of words with first and last characters are: ", count)