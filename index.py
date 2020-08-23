number = input("Введите первое число")
number2 = input("Введите второе число")

operand = input("Введите  оператор")
if operand == "*":
    print(int(number) * int(number2))
elif operand == "+":
    print(int(number) + int(number2))
elif operand == "-":
    print(int(number) - int(number2))
elif operand == "/":
    print(int(number) / int(number2))
