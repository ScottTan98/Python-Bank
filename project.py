import sys
import re
from tabulate import tabulate
import time


balance = 0

def main():
    table = [[1, "Deposit"],[2, "Withdraw"],[3, "Balance"],[4, "Exit"]]
    header = ["Select", "Menu"]
    while True:
        print(tabulate(table, header, tablefmt="outline"))
        selection = input("Choose Your Services: ")

        # Deposit
        if re.search(r"^[1-4]$", selection):
            if selection == "1":
                while True:
                    money = input("Deposit Amount: ")
                    if re.search(r"^[0-9]+$", money):
                        deposit(int(money))
                        print_slow(money, "deposit")
                        break
                    else:
                        print("input must be integer")

        # Withdraw
            elif selection == "2":
                while True:
                    money = input("Withdraw Amount: ")
                    if re.search(r"^[0-9]+$", money):
                        try:
                            withdraw(int(money))
                            print_slow(money, "withdraw")
                            break
                        except ValueError:
                            print("Input cannot be negative or less than balance")
                    else:
                        print("input must be integer")

        # View Balance
            elif selection == "3":
                print("$", balance )
                input("Press any keys back to menu")
        # Exit
            elif selection == "4":
                sys.exit()
        else:
            raise ValueError("Out of Selection")

def print_slow(amount, request):
    print(f"Processing ${amount} {request}", end="")
    for i in range(6):
        print(".", flush=True, end="")
        time.sleep(0.1)
    print("")

def deposit(money):
    global balance
    if money < 0:
        raise ValueError("Amount cannot be negative")
    else:
        balance += money
        return True


def withdraw(money):
    global balance
    if money < 0:
        raise ValueError("Amount cannot be negative")
    elif balance < money:
        raise ValueError("Amount not enough")
    else:
        balance -= money
        return True


if __name__ == "__main__":
    main()
