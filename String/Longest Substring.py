def longestSubstring(s):
    char_set = set()   # to store unique characters
    left = 0
    max_length = 0

    # right pointer expands window
    for right in range(len(s)):

        # if duplicate found → shrink window
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # add current character
        char_set.add(s[right])

        # update max length
        max_length = max(max_length, right - left + 1)

    return max_length


print(longestSubstring("abcabcbb"))