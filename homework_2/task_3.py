while True:
    year = input("Enter year: ").strip()
    if not year.isdigit() or year[0] == "0":
        print("Invalid input, try again")
    else:
        n = int(year)
        if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
            print("Leap year")
        else:
            print("Not a leap year")
        break
