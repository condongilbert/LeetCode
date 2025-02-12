def reverse(x):
    INT_MAX = -2**31, 2**31 - 1
    rev = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    
    while x != 0:
        digit = x % 10
        x //= 10
        
        # Check for overflow before multiplying
        if rev > (INT_MAX - digit) // 10:
            return 0
        
        rev = rev * 10 + digit

    return sign * rev