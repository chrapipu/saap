import numpy as np

# Вычисление z
a = 23.55
x = 0.9
z = -np.cbrt(x**3) + np.log(np.abs((a - 1.12 * x) / 4))
print("The value of z is:", z)

# Расчеты для линейной регрессии
X_column1 = np.ones((12, 1))
X_column2 = np.random.randint(21, 33, (12, 1))  # N варианта замените вашим номером варианта
X_column3 = np.random.randint(60, 82, (12, 1))
X = np.hstack((X_column1, X_column2, X_column3))
Y = np.random.uniform(13.5, 18.6, (12, 1))
A = np.linalg.inv(X.T.dot(X)).dot(X.T.dot(Y))
print("\nКоэффициенты линейной регрессии A:\n", A)

# Проверка вектора A
Y_check = X.dot(A)
print("\nПредсказанные значения Y:\n", Y_check)
print("\nИсходные значения Y:\n", Y)
