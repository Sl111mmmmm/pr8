while True:
    try:
        a = int(input("Введите первое целое число: "))
        b = int(input("Введите второе целое число: "))
        print(f"Сумма: {a + b}")
    except ValueError:
        print("Пожалуйста, вводите только целые числа.")
