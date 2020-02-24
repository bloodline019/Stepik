from pylab import *

figure()
x = arange(0, 160, 10)  # Создает массив от 0 до 150 (работает так же как и range()
x[0] = 1
y = round_((7.208 / (x + 45) ** 0.5), 3)
plot(x, y, "red")  # создает график по x и y с красным цветом
y = round_((7.39 / (x + 45) ** 0.5), 3)
plot(x, y, "green")
xlabel('Im')  # Определяем названия осей
ylabel("R")
print(x)  # Проверка ввеных массивов
print(y)
show()  # Вывод графика
