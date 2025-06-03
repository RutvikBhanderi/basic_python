def fibonacci_with_index(index):
    if index < 0:
        return "Index must be a non-negative integer."
    
    a, b = 1, 1
    series = []

    for i in range(index + 1):  
        series.append(a)
        a, b = b, a + b

    print("Fibonacci series up to index", index, ":")
    print(series)

    return series[index]

n = int(input("Enter the index of Fibonacci number to retrieve: "))
result = fibonacci_with_index(n)