def titleToNumber(columnTitle: str) -> int:
    ans, pos = 0, 0
    for letter in reversed(columnTitle):
        digit = ord(letter) - 64
        ans += digit * 26 ** pos
        pos += 1

    return ans

# one-liner
def excel_sheet_column_number(s):
    return sum((ord(c) - ord('A') + 1) * 26 ** i for i, c in enumerate(s[::-1]))

print(titleToNumber("ZY"))
print(excel_sheet_column_number("CX"))