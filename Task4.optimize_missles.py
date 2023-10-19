import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.widgets import Button

def read_objects(file_path):
    objects = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y, w = map(int, line.strip().split())
            objects.append((x, y, w))
    return objects

def calculate_strike_coordinates(objects, radius):
    max_damage = 0
    best_strike_x, best_strike_y = 0, 0

    for x in range(101):
        for y in range(101):
            total_damage = 0
            for obj_x, obj_y, obj_w in objects:
                distance = math.sqrt((x - obj_x)**2 + (y - obj_y)**2)
                if distance <= radius:
                    total_damage += obj_w

            if total_damage > max_damage:
                max_damage = total_damage
                best_strike_x, best_strike_y = x, y

    return best_strike_x, best_strike_y, max_damage

def update_radius(step):
    global current_radius
    current_radius += step
    if current_radius < 1:
        current_radius = 1
    if current_radius > 71:
        current_radius = 71
    strike_x, strike_y, total_damage = calculate_strike_coordinates(objects, current_radius)
    ax.clear()

    # Отображаем объекты военной инфраструктуры
    for obj_x, obj_y, obj_w in objects:
        obj_marker = ax.scatter(obj_x, obj_y, c='red', marker='o', s=obj_w/2, alpha=0.5, label=f'Object (Value={obj_w})')

    # Отображаем оптимальное местоположение удара
    ax.scatter(strike_x, strike_y, c='blue', marker='x', s=100, label=f'Strike (Total Damage={total_damage})')

    # Отображаем текущую координату
    ax.annotate(f'Current Coordinate: ({strike_x}, {strike_y})', xy=(strike_x, strike_y), xytext=(strike_x + 10, strike_y + 10),
                arrowprops=dict(arrowstyle='->'), fontsize=12)

    # Устанавливаем соотношение сторон графической области как 1:1
    ax.set_aspect('equal')

    # Отображаем радиус удара как круг
    strike_radius = Circle((strike_x, strike_y), current_radius, fill=False, color='green', linestyle='dashed', linewidth=2, label=f'Strike Radius (Radius={current_radius})')
    ax.add_patch(strike_radius)

    # Устанавливаем подписи к осям и заголовок
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.set_title(f"Military Infrastructure and Optimal Strike Location (Radius={current_radius})")
    ax.grid(True)
    #ax.legend()

    # Выводим урон на графике
    ax.text(0.7, 0.85, f"Total Damage: {total_damage}", transform=ax.transAxes, fontsize=12)

    # Перерисовываем график
    fig.canvas.draw_idle()

if __name__ == "__main__":
    file_path = r'C:\\Users\\smart\\OneDrive\\Рабочий стол\\GitTrue\\list2.txt'  # Замените на ваш путь к файлу с координатами

    objects = read_objects(file_path)
    current_radius = 1  # Начальный радиус
    max_damage_radius = 0
    max_damage_value = 0

    # Создаем график
    fig, ax = plt.subplots(figsize=(10, 6))

    # Создаем кнопки для увеличения и уменьшения радиуса
    ax_increase = plt.axes([0.7, 0.01, 0.1, 0.04])
    ax_decrease = plt.axes([0.81, 0.01, 0.1, 0.04])
    button_increase = Button(ax_increase, '+1')
    button_decrease = Button(ax_decrease, '-1')

    # Обработчики для кнопок
    def increase_radius(event):
        update_radius(1)

    def decrease_radius(event):
        update_radius(-1)

    button_increase.on_clicked(increase_radius)
    button_decrease.on_clicked(decrease_radius)

    # Подсчет урона и радиуса с наибольшим уроном
    for radius in range(1, 72):
        strike_x, strike_y, total_damage = calculate_strike_coordinates(objects, radius)
        if total_damage > max_damage_value:
            max_damage_value = total_damage
            max_damage_radius = radius

    update_radius(0)  # Обновляем график с начальным радиусом
    print(f"Radius with Maximum Damage: {max_damage_radius}, Maximum Damage Value: {max_damage_value}")

    # Показываем график
    plt.show()
