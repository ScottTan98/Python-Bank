# Bank.py
#### Video Demo:  https://youtu.be/QH2yQ7M6geg
#### Description:

A simple and easy bank program using python to let user to **deposit, withdraw, view** user's balance.

For this bank program is seperated into four part main, deposit, withdraw & view:

## **Main**

```python
def main():
    table = [[1, "Deposit"],[2, "Withdraw"],[3, "Balance"],[4, "Exit"]]
    header = ["Select", "Menu"]
    while True:
        print(tabulate(table, header, tablefmt="outline"))
        selection = input("Choose Your Services: ")
```

For the first part of the main, it designed to prompt user a table using `tabulate` libary & print out a GUI to show user few option.

It is looped using `while` loop, therefore if later user used any of the fuction, it will loop and reprompt the GUI to user again.

```
+----------+----------+
|   Select | Menu     |
+==========+==========+
|        1 | Deposit  |
|        2 | Withdraw |
|        3 | Balance  |
|        4 | Exit     |
+----------+----------+
Choose Your Services:
```
As from the terminal output above, there are 4 options & prompting the "Choose your Services:" is for the user to input for which selection they want to use.

## **Deposit**

```python
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
```

``` python
def deposit(money):
    global balance
    if money < 0:
        raise ValueError("Amount cannot be negative")
    else:
        balance += money
        return True
```
The code above will be indicate two section of the deposit function.

Before entering for the `deposit` function, the program will first check for the user whether user input only within the 4 selection that GUI that show before using the `regular expression` libary.

Then, if user selected `1` it will prompt user the deposit amount that user need just like as below
```
+----------+----------+
|   Select | Menu     |
+==========+==========+
|        1 | Deposit  |
|        2 | Withdraw |
|        3 | Balance  |
|        4 | Exit     |
+----------+----------+
Choose Your Services: 1
Deposit Amount:
```
user can input the amount of money they need to deposit. After that, the program will check the user using the same `regular expression`. If is valid, it will run the `deposit` function.

`deposit` function is fairly simple and easy which it job is add the valid amount that user prompt & add it to the current `balance`

`balance` is a variable that assign on top of the program with default value of 0, so the `deposit` function will update the latest state of the `balance`

## **Withdraw**
```python
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
```
```python
def withdraw(money):
    global balance
    if money < 0:
        raise ValueError("Amount cannot be negative")
    elif balance < money:
        raise ValueError("Amount not enough")
    else:
        balance -= money
        return True
```
`withdraw` function will be similar to `deposit`. When user selected `2`, it will prompt & ask user to enter amount of money user want to withdraw.

```
+----------+----------+
|   Select | Menu     |
+==========+==========+
|        1 | Deposit  |
|        2 | Withdraw |
|        3 | Balance  |
|        4 | Exit     |
+----------+----------+
Choose Your Services: 2
Withdraw Amount:
```
Same as `deposit` function, it will first check the input of the user are `int` & after it will check whether user withdraw amount is within the balance amount.

If `withdraw` is more than balance amount, it will reprompt and ask for input again with error message.

If is within the balance amount, it will continue run the `withdraw` function & deduct the withdraw amount that user input from the balance.

## **View**
```python
        # View Balance
            elif selection == "3":
                print("$", balance )
                input("Press any keys back to menu")

```

`view` section is to indicate user current balance that user have in their bank account.

When user selected `3`, it will prompt user current balance with the indication asking user to press any key to back to menu.


## **Exit**
```python
        # Exit
            elif selection == "4":
                sys.exit()
```

When user selected `4` it will exit the program completely.

## *Extra Feature*
```python
def print_slow(amount, request):
    print(f"Processing ${amount} {request}", end="")
    for i in range(6):
        print(".", flush=True, end="")
        time.sleep(0.1)
    print("")
```

This function feture code above is for delay a time using `time` libary which slow down the printing process which give user a better experience when they `deposit` or `withdraw` money from the program.

```
+----------+----------+
|   Select | Menu     |
+==========+==========+
|        1 | Deposit  |
|        2 | Withdraw |
|        3 | Balance  |
|        4 | Exit     |
+----------+----------+
Choose Your Services: 1
Deposit Amount: 1000
Processing $1000 deposit......
```
The function will print and show user the processing with the `.` will prompt one by one with time delay.




