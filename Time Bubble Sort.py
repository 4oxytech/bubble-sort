import timeit

#Время выполнения пузырьковой сортировки

time = """
def bubble_sort(array):
    N = len(array) #Число элементов в списке

    for i in range(0, N-1): #N-1 итераций работы алгоритма
        for j in range(0, N-1-i): #проход по оставшимся не отсортированным парам массива
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


array = [-9, 0, 5, 7, 1, 33, 55, 3, 6, 8, 98, -5, 9, 10, 31, 13] """

print(timeit.timeit(time, number=100)/100)

# ИТОГО: 4.6000000

#Время выполнения оптимизированной пузырьковой сортировки

time = """
def bubble_sort(array):
    flag = True
    N = len(array)

    while (flag):
        flag = False
        for i in range(N-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                flag = True

    return array

array = [-9, 0, 5, 7, 1, 33, 55, 3, 6, 8, 98, -5, 9, 10, 31, 13]"""

print(timeit.timeit(time, number=100)/100)
# ИТОГО: 2.409999

# Другая оптимизация пузырьковой сортировки

time = """
def bubble_sort(array):
    N = len(array)
    flag = True
    total_time = 0

    while (flag):
        flag = False
        for i in range(N - total_time - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                flag = True
        total_time += 1
    print("Кол-во итераций: ", total_time)

    return array

array = [-9, 0, 5, 7, 1, 33, 55, 3, 6, 8, 98, -5, 9, 10, 31, 13]"""

print(timeit.timeit(time, number=100)/100)

# ИТОГО: 2.339999