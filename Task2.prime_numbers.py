import math

def is_prime(num): #На вход в функцию подаётся целочисленное значение больше, либо = 1
    assert type(num) == int and num >= 1
    if num == 1:
        return False #Если число = 1, функция возвращает значение False (Число не является простым)
    sq = int(math.sqrt(num)) #Квадратный корень используем для оптимизации проверки на большие числа
    for i in range(2,sq + 1):
        if num % i == 0:
            return False
    return True #Функция возвращает значение True, если число является простым

def next_prime(num): #На вход в функцию подаётся целочисленное значение больше, либо = 1
    assert type(num) == int and num >= 1
    if num < 2:
        return 2  # Минимальное простое число больше 1 - это 2
    while not is_prime(num): #Используя цикл и прошлую функцию выясняем является ли число простым
        num += 1 
    return num #Функция возвращает значение следующего ближайшего простого числа

#def print_primes_until_max(max_num): #На входе в функцию подаётся целочисленное значение - число до которого будут перебираться простые числа
    if not isinstance(max_num, int) or max_num < 1:
        return None
    
    prime = find_next_prime(1)
    while prime <= max_num:
        print(prime)
        prime = find_next_prime(prime)

# Пример использования:
#max_num = 2**63 - 1
#print_primes_until_max(max_num)

def gcd(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise AssertionError
    a = abs(a)
    b = abs(b)
    if a == 0 or b == 0:
        return max(a, b)
    gcd_meaning = 1
    a_fact = a
    b_fact = b
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0 and is_prime(i):
            while a_fact % i == 0 and b_fact % i == 0:
                gcd_meaning *= i
                a_fact //= i
                b_fact //= i
    return gcd_meaning


def are_coprime(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise AssertionError
    a = abs(a)
    b = abs(b)
    if gcd(a, b) == 1:
        return True
    return False
