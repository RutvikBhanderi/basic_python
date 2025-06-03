def sum_divided_c(a,b,c):
    total = 0
    for num in range(a,b ):
        if num % c == 0:
            total += num
    return total

a = int(input("Enter number for a:"))
b = int(input("Enter number for b:"))
c = int(input("Enter number for c:"))