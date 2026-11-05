import random

numbers = []
for i in range(5):
    numbers.append(random.randint(1,4))

print("First list: " + str(numbers))

new_numbers = []
for num in numbers:
    for i in range(num):
        new_numbers.append(num)

print("Second list: " + str(new_numbers))
print("Length is : " + str(len(new_numbers)))
