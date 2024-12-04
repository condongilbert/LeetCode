def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Compute prefix product
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Compute postfix product
    postfix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result

# Test the function
nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]