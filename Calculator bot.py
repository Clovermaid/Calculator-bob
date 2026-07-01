#Calculator bot
bot_name: str = 'Calc bob'
print(f'Hello, i am {bot_name} and im your calc bot, what can i do today?')
print('do to limations of my creator i can only do basic math opertaions and two inputs sorry!')
print('you can start by typing anything')
print('type + for addition, - for subtraction, * for multiplication and / for division')
while True:
    operation = input("You: ")

    if operation.lower() == "exit":
        break

    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))

        if operation == "+":
            print(num1 + num2)
        elif operation == "-":
            print(num1 - num2)
        elif operation == "*":
            print(num1 * num2)
        elif operation == "/":
            print(num1 / num2)
        else:
            print("Unknown operation.")

    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
        print("You can't divide by zero!")