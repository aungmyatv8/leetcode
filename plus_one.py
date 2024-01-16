def increment_large_integer(digits):
    # Reverse the digits to start from the least significant digit.
    digits = digits[::-1]
    print(digits)
    carry = 1
    result = []
    
    for digit in digits:
        current_sum = digit + carry
        result.append(current_sum % 10)
        carry = current_sum // 10
    
    # If there's still a carry after the loop, add it as a new digit.
    if carry:
        result.append(carry)
    
    # Reverse the result to get the correct order.
    return result[::-1]

# Example usage:
large_integer = [1, 2, 3]
result = increment_large_integer(large_integer)

print(f"The incremented large integer is: {result}")
