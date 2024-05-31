def row_sum_odd_numbers(n):
    first_number = n**2 - n + 1
    
    # The sum of the numbers in the nth row is given by n * (2*first_number + (n-1)*2) / 2
    sum_numbers = n * (2 * first_number + (n - 1) * 2) / 2
    
    return int(sum_numbers)
row_sum_odd_numbers(3)