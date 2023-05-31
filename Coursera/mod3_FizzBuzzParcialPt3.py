numb = int(input("Digite um número: "))


if numb%5 == 0 and numb%3 == 0:
    print("FizzBuzz")
else:
    if numb%5 == 0:
        print("Buzz")
    if numb%3 == 0:
        print("Fizz")
if numb%5 != 0 and numb%3 != 0:
    print(numb)