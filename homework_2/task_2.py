while True:
    num = input("Enter a number: ").strip()
    if not num.isdigit() or int(num) <= 0 or num[0] == "0" or int(num) > 1000:
        print("Invalid input, try again")
    else:
        div = set()
        n = int(num)
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                div.add(i)
                div.add(n // i)
        print(sorted(div))
        print("total number of divisors: " + str(len(div)))
        break



