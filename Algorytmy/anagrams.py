def verify_anagrams(first_word, second_word):
    first_word = first_word.lower()
    second_word = second_word.lower()
    first_word = list(first_word)
    second_word = list(second_word)
    first_word = [ i for i in first_word if (i != ' ') ]
    second_word = [ i for i in second_word if (i != ' ') ]
    first_word.sort()
    second_word.sort()
    return (first_word == second_word)
