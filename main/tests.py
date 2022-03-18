def tasks(numbers) -> list:
    print(type(numbers))
    return sum(numbers)


# print(tasks([1,2,3,5,6,78,6]))
def task2(numbers) -> list:
    for i in numbers:
        if i < 0:
            print(i)
    # task2([1,2,34,-6,7,-2])
    # def task3(numbers)->list:
    for i in numbers:
        if i % 2 == 0:
            print(i)


# task3([1,2,34,-6,7,-2])
def task4(x: int, y: int) -> float:
    print((x + y) / 2)


# task4(2,8)
def task5(words) -> str:
    print(words[::-1])


# task5('Hello')
def task6(s) -> str:
    l = len(s)
    integ = []
    i = 0
    while i < l:
        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            integ.append(int(s_int))

    print(integ)


# task6('Hello123ds12')
def tasks7(words) -> str:
    reverse_words = words[::-1]
    if words == reverse_words:
        print('Это полиндром')
    else:
        print('Не палиндром')


def tesk8(arr, arr_size, sum):
    hashmap = {}

    for i in range(0, arr_size):
        temp = sum - arr[i]
        if (temp in hashmap):
            print(f'Пара с заданной суммой {sum} равна ({temp},{arr[i]}) по индексам ({hashmap[temp]},{i})')
        hashmap[arr[i]] = i


A = [1, 4, 45, 6, 10, 8]
n = 16
#tesk8(A, len(A), n)
def task9(words):
    words = list(words)

    for i in words:
        if i == '#':
            words.remove(i)
    my_list = [''.join(words)]
    print(my_list)
#task9('#qwer#rty')

def task10(numbers:list):
    for i in numbers:
        if numbers.count(i) > 1:
            print(f'{i} -> {numbers.count(i)}')
task10([1,2,3,2,2,3,4])








