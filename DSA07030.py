class Person:
  name = "John"
  age = 36
  country = "Norway"
setattr(Person, age)
p = Person
print(p.age)