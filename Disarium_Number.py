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
