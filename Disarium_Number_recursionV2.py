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
