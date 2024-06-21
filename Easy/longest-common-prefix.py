def longest_common_prefix(strs):
    if not strs:
        return ""

    if len(strs) == 1:
        return strs[0]

    strs.sort()
    first_str = strs[0]
    last_str = strs[-1]
    prefix = ""
    for i in range(len(first_str)):
        if i < len(last_str) and first_str[i] == last_str[i]:
            prefix += first_str[i]
        else:
            break

    return prefix


strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))
