a = int(input("Введите первое целое число (a): "))
b = int(input("Введите второе целое число (b): "))

start = min(a, b) + 1
end = max(a, b)

for number in range(start, end):
    print(number)
