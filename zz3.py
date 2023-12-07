import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# №1
x = 12.1
c = -10
c_values = []  # Создаем список для хранения значений c
Fun_x = np.array([])  # Инициализируем пустой массив для Fun_x

while c <= 1:
    f = pow(np.fabs(2 * x + c), 3) ** (1/5) + 0.567
    Fun_x = np.append(Fun_x, f)
    c_values.append(c)  # Добавляем c в список
    c += 0.5

X = np.array(c_values)  # Преобразуем список c_values в массив NumPy

Res = pd.DataFrame({"c": X, "f(x)": Fun_x})
print(Res)
print("Наибольшее значение - {}".format(Fun_x.max()))
print("Наименьшее значение - {}".format(Fun_x.min()))
print("Среднее значение - {}".format(Fun_x.mean()))
print("Количество элементов массива значений функции f(c) - {}".format(Fun_x.size))
print("Отсортированный по убыванию numpy-массив функций f(c)\n", np.sort(Fun_x, axis=-1))

plt.plot(X, Fun_x, label="-10 <= c <= 1; 1 <= f(c) < 734")
plt.axhline(y=Fun_x.mean(), color="green", label="среднее значение f(c)")
plt.title("График изменения значений функции f(c)")
plt.xlabel("Значение аргумента c")
plt.ylabel("Значение функции f(c)")
plt.legend(loc="upper right", frameon=False)
plt.show()

# №2
u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
x = np.cos(u) * np.sin(v)
y = np.cos(v) * np.sin(u)
z1 = x ** 0.25 + y ** 0.25
z2 = x ** 2 - y ** 2
z3 = 2 * x + 3 * y
z4 = x ** 2 + y ** 2
z5 = 2 + 2 * x + 2 * y - x ** 2 - y ** 2
fig = plt.figure()
ax = fig.add_subplot(2, 2, 1, projection='3d')
ax.plot_surface(x, y, z1)
ax = fig.add_subplot(2, 2, 2, projection='3d')
ax.plot_wireframe(x, y, z2)
ax = fig.add_subplot(2, 2, 3, projection='3d')
ax.plot_wireframe(x, y, z3)
ax = fig.add_subplot(2, 2, 4, projection='3d')
ax.scatter(x, y, z4)
ax = fig.add_subplot(2, 1, 1, projection='3d')
ax.plot_surface(x, y, z5)
plt.show()
