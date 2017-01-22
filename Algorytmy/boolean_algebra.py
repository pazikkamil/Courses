OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")





def boolean(x, y, operation):

    wynik = 0

    if (operation == "conjunction"):

        wynik = x and y

    elif (operation == "disjunction"):

        wynik = x or y

    elif (operation == "implication"):

        wynik = not(x) or y

    elif (operation == "exclusive"):

        wynik = x ^ y

    elif (operation == "equivalence"):

        wynik = (x == y)

    return int(wynik)





if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing

    assert boolean(1, 0, "conjunction") == 0, "and"

    assert boolean(1, 0, "disjunction") == 1, "or"

    assert boolean(1, 1, "implication") == 1, "material"

    assert boolean(0, 1, "exclusive") == 1, "xor"

    assert boolean(0, 1, "equivalence") == 0, "same?"



    print("All done? Earn rewards by using the 'Check' button!")


