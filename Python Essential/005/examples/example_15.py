# setattr(object, name, value)
class Person:
    name = 'Petro'


p = Person()
# Before modification: Petro
print('Before modification:', p.name)
setattr(p, 'name', 'Ivan')
# After modification: Ivan
print('After modification:', p.name)
