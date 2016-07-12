def main():
    print('Select from  the list below which operation you want the calculator to do.')
    print("A.Add")
    print("S.Subtract")
    print("M.Multiply")
    print("D.Divide")
    while True:
        choice = input("Enter choice(a/s/m/d)")
        if choice not in {"a", "s", "m", "d","q"}:
            print (" the letter you entered is not in our lists!")
            continue
        num1 = int(input("Enter an integer as your first number: "))
        num2 = int(input("Enter an integer as second number: "))
        if choice == 'a':
            print("{} + {} = {}".format(num1, num2, add(num1, num2)))
        elif choice == 's':
            print("{} - {} = {}".format(num1, num2, subtract(num1, num2)))
        inp = input("Enter 1 to play again or 2 to exit")
        if inp == "1":
            main()
        else:
            print("thanks for playing")
            break

main()
