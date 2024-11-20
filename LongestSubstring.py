def length_of_longest_substring(s: str) -> int:
    char_index = {}
    max_length = 0
    start = 0  # Start index of the sliding window

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            # Move the start to avoid duplicate
            start = char_index[s[end]] + 1
        # Update the current character's index
        char_index[s[end]] = end
        # Calculate the current window length
        max_length = max(max_length, end - start + 1)

    return max_length