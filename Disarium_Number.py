# Disarium Number
# A number is said to be Disarium if the sum of its digits raised to their
# respective positions is the number itself.
# Challenge is to create a function to identify if a number is Disarium or not
# Example input: 75 > 7^1 + 5^2 = 7 * 25 = 32 = False
# listed under "Hard" on https://edabit.com/challenge/yvJbdkmKHvCNtcZy9
def is_disarium_basic(n):
    """first attempt"""
    num = list(str(n))
    num_final = []
    for index, char in enumerate(num):
        digit = int(char)
        result = digit**(index + 1)
        num_final.append(result)
    if sum(num_final) == int(n):
        return True
    else:
        return False

def is_disarium_pythonic(n):
    """second attempt using Pythonic code, still working on this"""
    num = str(n)
    num_final = [int(char) ** (index + 1) for index, char in enumerate(num)]
    return sum(num_final) == int(n)

def is_disarium_recursion(n):
    """Third attempt using recursion"""
    def calc_disarium_sum(num_str, index=1):
        if not num_str:
            return 0
        current_power = int(num_str[0]) ** index
        return current_power + calc_disarium_sum(num_str[1:], index + 1)
    return calc_disarium_sum(str(n)) == int(n)

def is_disarium_recursion_v2(n, original_n=None, index=1):
    """Recursion attempt 2 using the original function to track the location of the digit instead of a wrapper function."""
    num_str = str(n)
    if original_n is None:
        original_n = n
    if not num_str:
        return original_n == 0
    current_power = int(num_str[0]) ** index
    if len(num_str) == 1:
        return current_power == original_n
    return is_disarium_recursion_v2(num_str[1:], original_n - current_power, index + 1)
