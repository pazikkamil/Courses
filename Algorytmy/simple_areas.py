import math
def angles(a, b, c):
    # 2*pi*rad = 360 stopni
    # c ** 2 = a ** 2 + b ** 2 - 2*a*b *math.cos(
    # c = (a ** 2 + b**2 - (2*a*b*math.cos(gamma)) ** (1.0/2.0)
    pole = 0
    try:
        cos_gamma = ( a**2 + b**2 - c**2)/ float(2*a*b)
        kat_gamma = math.acos(cos_gamma)
        pole = 0.5 * a* b * math.sin(kat_gamma)
    except:
        pole = 0
    return pole

def simple_areas(*args):
    argsNum = len(args)
    result = 0
    if (argsNum == 1):
	    result = math.pi * ((args[0]/2.00) ** 2)
    elif (argsNum == 2):
	    result = (args[0] * args[1])
    elif (argsNum == 3):
	    result = angles(args[0], args[1], args[2])
    return round(result, 2)
    
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"

    print("Earn cool rewards by using the 'Check' button!")

