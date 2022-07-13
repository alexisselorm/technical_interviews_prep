from numpy import character


def romanToInt(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    result = 0
    for i in range(len(s)):
        if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            result -= roman[s[i]]
        else:
            result += roman[s[i]]

# Comments
# the value at roman i where s is the key
# roman[s[i]]
# If it is smaller than the next one decrease  the result because it's not supposed to happen
# else increase
