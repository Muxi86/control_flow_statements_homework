def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    S = 0
    if a < 0:
        S += 1
    if b < 0:
        S += 1
    if c < 0:
        S += 1
    return S

a = int(input('a ='))
b = int(input('b ='))
c = int(input('c ='))

print(main(a,b,c))