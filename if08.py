def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a > 9 and a < pow(10,2) and a%2 != 0:
        return "two-digit odd number"
    if a > 9 and a < pow(10,2) and a%2 == 0:
        return "two-digit even number"
    if a >= pow(10,2) and a < pow(10,3) and a%2 != 0:
        return "two-digit odd number"
    if a >= pow(10,2) and a < pow(10,3) and a%2 == 0:
        return "two-digit even number"

a = int(input())
print(main(a))
