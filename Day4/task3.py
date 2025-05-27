def duplicate_nums(nums):
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    if duplicates:
        return sorted(duplicates)
    else:
        return None

print(duplicate_nums([1,10,12,10,11,15,32,32,20]))                     
print(duplicate_nums([18,19,20,21,21,21,22,25,26,25,63,89,63])) 
print(duplicate_nums([10,20,30,40,50,60,70]))       