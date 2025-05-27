def generate_product_id(flavor, capacity):
    words = flavor.split()
    product_code = ''.join([word[:3].upper() for word in words])
    
    
    return product_code + capacity

print(generate_product_id("apple", "500ml"))  
print(generate_product_id("pineapple", "45ml"))  
print(generate_product_id("passion fruit", "750ml"))  