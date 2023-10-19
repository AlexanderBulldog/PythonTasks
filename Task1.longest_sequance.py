def get_seq_len(n): # Первая функция, подсчитывает количество шагов в целом по поданному значению n
    if not isinstance(n, int) or n <= 0:
            return None
    steps = 0 # Переменная счётчика
    while n != 1:  # Цикл до тех пор пока число n не будет равно 1
        if n % 2 == 0: # Проверка на чётность, если число чётное, делим его на 2
            n = n // 2
        else: # Если число нечётное, проводим следущую операцию
            n = 3 * n + 1
        steps += 1
    return steps + 1 # Возвращаем значение счётчика (Количество шагов)

def get_longest_seq(a, b): # Функция для получения самого большого числа шагов
    if type(a) != int or type(b) != int:
        return None
    if a <= 0 or b <= 0:
        return None
    if b < a:
        return None
    max_steps = 0 # Переменная счётчик для максимальных шагов
    number_with_max_steps = 0 # Переменная для запоминания числа с наибольшим числом шагов

    for num in range(a, b + 1): # Цикл, который перебирает значения от a до b (включительно)
        steps = get_seq_len(num) # Вызывается функция, которая считает значения для каждого num в цикле
        if steps > max_steps:
            max_steps = steps
            number_with_max_steps = num

    return number_with_max_steps, max_steps # Функция возвращает два значения - максимальное количество шагов и число с наибольшим количеством шагов