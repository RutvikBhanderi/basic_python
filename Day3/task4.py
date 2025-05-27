def sum_even_odd(number):
    even_sum = 0
    odd_sum = 0

    for x in number:
        if x % 2 == 0:
            even_sum += x
        else:
            odd_sum += x
    
    return[even_sum,odd_sum]

number = [1,20,31,40,51,60,71,80,90]
result =sum_even_odd(number)
print(f"the sum of even num: {result[0]}, the sum of odd num: {result[1]}")
