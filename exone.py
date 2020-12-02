result = []


# Adds two numbers
def add(x, y):
    return x + y

# Subtract two numbers
def subtract(x, y):
    return x - y

# Multiplie two numbers
def multiply(x, y):
    return x * y

# Divide two numbers
def divide(x, y):
    return x / y

print("Choose numbers 1, 2, 3, 4")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            x =  add(num1, num2)
            result.append(x)
            print(num1, "+", num2, "=", x )

        elif choice == '2':
            w = subtract(num1, num2)
            result.append(w)
            print(num1, "-", num2, "=", w)

        elif choice == '3':
            e = multiply(num1, num2)
            result.append(e)
            print(num1, "*", num2, "=", e)

        elif choice == '4':
            r = divide(num1, num2)
            result.append(r)
            print(num1, "/", num2, "=", r)
        break

    else:
        print("Invalid Input" " Try insted 1-2-3-4")

number = sum(result)

if number < 50:
    print("Less then fifty")

elif number == 50:
    print("Fifty")

elif number == 100:
    print("Spot on!")

elif number > 100:
    print ("Missed the spot!")

elif number > 50 and number < 100:
    print ("Almost a hundred")
