def spin_words(slova):
    word = slova.split()
    for i in range(len(word)):
        if len(word[i]) > 5:
            word[i] = word[i][::-1]
    return word
