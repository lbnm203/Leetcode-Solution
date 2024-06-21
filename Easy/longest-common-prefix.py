def longest_common_prefix(strs):
    f_str = strs[0]
    l_str = strs[-1]
    lst = ""
    for i in range(len(strs)):
        if f_str[i] != l_str[i]:
            break
        else:
            lst += f_str[i]
    return lst


strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))
