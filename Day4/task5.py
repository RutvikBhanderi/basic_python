def sum_of_evens(matrix):
    total = 0
    for row in matrix:
        for num in row:
            if num % 2 == 0:
                total += num
    return total

print(sum_of_evens([[1,2,3],[4,5,6],[7,8,9]]))
print(sum_of_evens([[22,21],[23,23]]))
print(sum_of_evens([[],[]]))