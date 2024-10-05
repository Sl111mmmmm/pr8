i = 0

while True:
    vvodi = input("Введите число (или 'stop' для завершения): ")
    
    if vvodi.lower() in ['stop', 'end']:
        break
    
    try:
    
        number = float(vvodi) 
        i += number
    except ValueError:
        print("Пожалуйста, введите корректное число.")

print(f"Сумма введенных чисел: {i}")
