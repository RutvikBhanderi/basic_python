def max_difference(tupList):
    max_diff = float('-inf')  
    for tup in tupList:
        diff = abs(tup[0] - tup[1])  
        if diff > max_diff:
            max_diff = diff
    return max_diff

tupList = [(90, 7), (2, 60.5), (1, 9), (1, 3)]
result = max_difference(tupList)
print(result)