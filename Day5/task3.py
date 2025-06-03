def count_data_types(*args):
    type_counts = {}

    for arg in args:
        data_type = type(arg).__name__  
        if data_type in type_counts:
            type_counts[data_type] += 1
        else:
            type_counts[data_type] = 1

   
    return list(type_counts.items())

print(count_data_types(1, "hello", 3.14, True, [1, 2], 2, False, "world"))
