def merge(str1, str2):
    i, j = 0,0
    res = ''

    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            new_i, new_j = i, j
            while  new_i < len(str1) and new_j< len(str2) and str1[new_i] == str2[new_j]:
                res += str1[new_i]
                new_i += 1
                new_j += 1
            
            if new_j == len(str2): 
                res += str1[i:]
                return res
            elif new_i == len(str1):
                res += str2[j:]
                return res
            else:
                if str1[new_i] > str2[new_j]:
                    res += str1[new_i]
                    i = new_i + 1
                else:
                    res += str2[new_j]
                    j = new_j + 1

            pass
        elif str1[i] > str2[j]:
            res += str1[i]
            i += 1
        else: 
            res += str2[j]
            j += 1

    if i == len(str1): 
        res += str2[j:]
        return res
    else:
        res += str1[i:]
        return res

# "uuug"
# "gggu"
# 0,0 -> 1, 0 -> 2, 0
# res = uu