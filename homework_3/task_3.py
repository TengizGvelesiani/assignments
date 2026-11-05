text = input("Input: ").lower()
cleaned = ""
for char in text:
    if char.isalpha():
        cleaned += char

rev = cleaned[::-1]
if rev == cleaned:
    print("Output: Is palindrome")
else:
    print("Output: Is not palindrome")