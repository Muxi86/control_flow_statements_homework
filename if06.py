def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    S = 0
    if a > 0:
        S += 1
    if b > 0:
        S += 1
    if c > 0:
        S += 1
    if S >= 3-S:
        return "there are a lot of positive numbers"
    else:
        return "there are a lot of negative numbers"

a = int(input('a ='))
b = int(input('b ='))
c = int(input('c ='))

print(main(a,b,c))