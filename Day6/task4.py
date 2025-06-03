class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

def people_sort(people_list, attribute):
    return sorted(people_list, key=lambda person: getattr(person, attribute))

p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)

sorted_by_firstname = people_sort([p1, p2, p3], "firstname")
sorted_by_lastname = people_sort([p1, p2, p3], "lastname")
sorted_by_age = people_sort([p1, p2, p3], "age")

print([p.firstname for p in sorted_by_firstname])  
print([p.lastname for p in sorted_by_lastname])    
print([p.age for p in sorted_by_age])  