def lengthOfLongestSubstring(s):
    if len(s) <= 1:
        return len(s)

    longest = 0
    left = 0
    seenChars = {}

    for right in range(0, len(s)):
        currChar = s[right]
        prevSeenChar = -1
        if currChar in seenChars.keys():
            prevSeenChar = seenChars[currChar]

        if prevSeenChar >= left:
            left = prevSeenChar + 1

        seenChars[currChar] = right
        longest = max(longest, right - left + 1)
    return longest

print(lengthOfLongestSubstring("abcabcbb"))