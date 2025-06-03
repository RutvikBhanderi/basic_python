def count_duplicates(s):
    seen = set()
    duplicate = set()

    for char in s:
        if char in seen:
            duplicate.add(char)
        else:
            seen.add(char)
    return len(duplicate)

print(count_duplicates("hrlooooloee"))
print(count_duplicates("india"))
print(count_duplicates("usa"))
