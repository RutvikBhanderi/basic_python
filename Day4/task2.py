def count(n):
    n = abs(n)  
    if n == 0:
        return 1 
    digits = 0
    while n > 0:
        n //= 10
        digits += 1
    return digits

print(count(3201))       
print(count(-23156))    
print(count(22))      