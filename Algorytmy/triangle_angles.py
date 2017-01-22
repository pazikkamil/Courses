import math
def angles(a, b, c):
    # 2*pi*rad = 360 stopni
    # c ** 2 = a ** 2 + b ** 2 - 2*a*b *math.cos(
    # c = (a ** 2 + b**2 - (2*a*b*math.cos(gamma)) ** (1.0/2.0)
    try:
        cos_gamma = ( a**2 + b**2 - c**2)/ float(2*a*b)
        kat_gamma = round(math.acos(cos_gamma) * 180 / math.pi)
        cos_beta = ( b**2 + c**2 - a**2)/ float(2*b*c)
        kat_beta = round(math.acos(cos_beta) * 180 / math.pi)
        kat_alfa = 180 - kat_gamma - kat_beta
        lista = [kat_gamma, kat_beta, kat_alfa]
        lista.sort()
    except:
        lista = [0, 0, 0]
    if ([ i for i in lista if(i<=0)]):
        lista = [0, 0, 0] 
    return lista


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It can not be a triangle"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")

