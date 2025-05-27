def swap(txt, c1, c2):
    swapped = []
    for x in txt:
        if x == c1:
            swapped.append(c2)
        elif x == c2:
            swapped.append(c1)
        else:
            swapped.append(x)
    return ''.join(swapped)

print(swap("indianiiii", "i" , "j"))
print(swap("123,563,258,465,254,568,154",'3','8'))