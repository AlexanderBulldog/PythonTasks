import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Параметры модели Лоренца
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Начальные условия
x0, y0, z0 = 0, 1, 1.05
t0, t_max, dt = 0.0, 100.0, 0.01

# Создаем массивы для хранения данных
t_values = np.arange(t0, t_max, dt)
x_values, y_values, z_values = [], [], []

# Инициализируем начальные значения
x, y, z = x0, y0, z0

# Численно решаем уравнения Лоренца и сохраняем данные
for t in t_values:
    x_values.append(x)
    y_values.append(y)
    z_values.append(z)
    
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    
    x += dx * dt
    y += dy * dt
    z += dz * dt

# Создаем функцию инициализации для анимации
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

# Создаем функцию обновления для анимации
def update(num, x_values, y_values, z_values, line):
    line.set_data(x_values[:num], y_values[:num])
    line.set_3d_properties(z_values[:num])
    return line,

# Создаем график и анимацию
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
line, = ax.plot([], [], [], lw=0.5)

# Устанавливаем пределы для графика
ax.set_xlim(min(x_values), max(x_values))
ax.set_ylim(min(y_values), max(y_values))
ax.set_zlim(min(z_values), max(z_values))

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Анимация аттрактора Лоренца')

ani = FuncAnimation(fig, update, frames=len(t_values), init_func=init, fargs=(x_values, y_values, z_values, line), interval=0.01, blit=True)

# Отображаем анимацию
plt.show()