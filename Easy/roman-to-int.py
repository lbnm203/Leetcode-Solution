def roman_to_int_func(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(s)):
        curr_values = roman[s[i]]

        if i + 1 < len(s) and curr_values < roman[s[i+1]]:
            total -= curr_values
        else:
            total += curr_values

    return total


# show result
s = "MCMXCIV"
result = roman_to_int_func(s)
print(result)
