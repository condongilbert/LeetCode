def is_leap(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If divisible by 4, check if it's divisible by 100
        if year % 100 == 0:
            # If divisible by 100, check if it's divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Example usage:
year = int(input("Enter a year: "))
print(is_leap(year))