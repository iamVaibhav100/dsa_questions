# Q4 Given two strings sand t, return true if they are equal when both are typed into empty
# text editors.'#'means a backspace character.

# Optimized space solution

def backspaceCompare(s1, s2):
    # get last index of both strings
    r1 = len(s1) - 1
    r2 = len(s2) - 1

    # iterate until index of both strings are out of range
    while r1 >= 0 or r2 >= 0:
        # init empty char
        c1, c2 = "", ""
        # check if pointer is within bounds
        if r1 >= 0:
            # get the processed character and corresponding pointer (index)
            # returned pointer would update the index
            c1, r1 = getChar(s1, r1)
        if r2 >= 0:
            c2, r2 = getChar(s2, r2)
        # if char does not match, return Falsy
        if c1 != c2: return False
    # return Truthy if no mismatch was found so far
    return True


def getChar(s, r):
    # init char and count
    char, count = '', 0
    # iterate until char is empty and pointer is within bounds
    while r >= 0 and not char:
        # check if current char is "#"
        # if yes, update the counter
        # counter is used to skip the next real-char
        if s[r] == '#':
            count += 1
        # if counter is zero and real-char, assign val to "char" var
        elif count == 0:
            char = s[r]
        # if counter > 0 and current is real-char, decrement the counter
        else:
            count -= 1
        # shift the pointer for each iteration
        r -= 1
    return char, r