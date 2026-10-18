def is_disarium_pythonic(n):
    """second attempt using Pythonic code, still working on this"""
    num = str(n)
    num_final = [int(char) ** (index + 1) for index, char in enumerate(num)]
    return sum(num_final) == int(n)
