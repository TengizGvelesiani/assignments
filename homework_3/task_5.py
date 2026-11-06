first = input("First string: ").lower()
second = input("Second string: ").lower()

first_map = {}
second_map = {}
for char in first:
    first_map[char] = first_map.get(char, 0) + 1

for char in second:
    second_map[char] = second_map.get(char, 0) + 1

if first_map == second_map:
    print("Output: YES")
else:
    print("Output: NO")