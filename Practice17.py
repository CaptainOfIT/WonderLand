def sort_by_inserts(list_input):
    list_int = list_input
    for i in range(1, len(list_int)):
        x = list_int[i]
        idx = i
        while idx > 0 and list_int[idx - 1] > x:
            list_int[idx] = list_int[idx - 1]
            idx -= 1
        list_int[idx] = x
    return list_int

def binary_search(array, element, left, right):
    if left > right: # если левая граница превысила правую,
        return False # значит элемент отсутствует

    middle = (right+left) // 2 # находимо середину
    if array[middle] == element: # если элемент в середине,
        return middle # возвращаем этот индекс
    elif element < array[middle]: # если элемент меньше элемента в середине
# рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle-1)
    else: # иначе в правой
        return binary_search(array, element, middle+1, right)

def int_verify(str_in):
    try:
        str_int = int(str_in)
        return str_int
    except ValueError:
        print(f"Данное число '{str_in}' невозможно преобразовать в целое")
        return None

while True:
    str_ = input("Введите целые числа через пробел: ").split()
    try:
        num_ = list(map(int_verify, str_))
        if not num_ or None in num_:
            print("Числа введены неверно!")
    except ValueError:
        print ("Вы вввели не число! Попробуйте снова. ")
    else:
        sequence_sorted = sort_by_inserts(num_)
        print("Сортировка списка по возрастанию в нем элементов: ", sequence_sorted)
        break

str_ = input("Введите целое число для поиска в отсортированном списке: ")
cfr_ = int_verify(str_)
if cfr_ == None:
    print("Число введено неверно!")
if num_[0] >= cfr_ or num_[-1] < cfr_:
    print("Элемент не найден!")
else:
    for i in range(cfr_ - 1, num_[0] - 1, -1):
        idx = binary_search(num_, i, 0, len(num_))
        if idx != None:
            print(f"Номер позиции равен {idx} (элемент {i})")
            break