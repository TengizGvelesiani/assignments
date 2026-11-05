num = input("Enter a number: ")
seq = [0, 1]
if not num.isdigit() or int(num) <= 0  or num[0] == "0" or int(num) > 100:
    print("Invalid input, try again")
else:
    if int(num) == 1:
        print("[0]")
    elif int(num) == 2:
        print("[0, 1]")
    else:
        n = int(num) - 2
        for i in range(n):
            seq.append(seq[i] + seq[i + 1])
        print(seq)

