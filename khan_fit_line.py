import statistics as st
import numpy as np
import matplotlib.pyplot as plt

def xy_sum(x, y):
    xysum = 0
    for i in range(len(x)):
        xysum = xysum + x[i] * y[i]
    return xysum

def x2_sum(x):
    x2sum = 0
    for i in range(len(x)):
        x2sum = x2sum + x[i] * x[i]
    return x2sum

def fitted(x, y):
    beta = ((sum(y) / len(x)) * x2_sum(x) - st.mean(x) * xy_sum(x, y)) / (x2_sum(x) - len(x) * (sum(x) / len(x)) ** 2)
    alpha = (xy_sum(x, y) - beta * len(x) * (sum(x) / len(x))) / x2_sum(x)
    return alpha, beta

x_new = []
y_new = []

def mouse(click):
    if click.button == 1:
        x_new.append(click.xdata)
        y_new.append(click.ydata)
        plt.clf()
        plt.scatter(x_new, y_new, marker='o')
        plt.xticks(range(-3, 7, 1))
        plt.yticks(range(-3, 7, 1))
        plt.draw()
    elif click.button == 3:
        plt.close()

plt.figure()
plt.xticks(range(-3, 7, 1))
plt.yticks(range(-3, 7, 1))
plt.scatter(x_new, y_new, marker='o')
plt.gcf().canvas.mpl_connect('button_press_event', mouse)
plt.show()



plt.figure()
alpha, beta = fitted(x_new, y_new)
xn = np.arange(-2, 5, 0.1)
plt.plot(xn, alpha * xn + beta, color='blue')
plt.scatter(x_new, y_new, label='points')
print(f"Fitted line is: a = {alpha} and b = {beta}")
plt.draw()
plt.show()        