S = 0
Price = None
a = None
b = 0
c = 990
d = 1390

Tickets = int(input("Введите количество билетов, которое вы желаете приобрести: \n"))
for i in range(Tickets):
    a = int(input("Введите возраст посетителя от 0 до 100: \n"))
    if 0 <= a < 18:
        Price = b
        S += Price
    if 18 <= a < 25:
        Price = c
        S += Price
    if 25 <= a <= 100:
        Price = d
        S += Price
if Tickets <= 3:
    print("Общая стоимость билетов - ", round(S, 0), "руб.")
else:
    S = S - (0.1 * S)
    print("Общая стоимость билетов со скидкой 10% - ", int(S), "руб.")


