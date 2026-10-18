def is_disarium_recursion(n):
    """Third attempt using recursion"""
    def calc_disarium_sum(num_str, index=1):
        if not num_str:
            return 0
        current_power = int(num_str[0]) ** index
        return current_power + calc_disarium_sum(num_str[1:], index + 1)
    return calc_disarium_sum(str(n)) == int(n)
