import matplotlib.pyplot as plt
import numpy as np


def f(x_arg):
    y_tmp = 2 * x_arg
    # y_tmp = x_arg * 2 + 5
    return y_tmp


def draw_function(max):
    x = np.arange(0, max, 0.1)
    plt.plot(x, f(x))


def is_under(arg_x, arg_y):
    if arg_y <= f(arg_x):
        return True
    else:
        return False

plt.ion() ## Note this correction
fig=plt.figure()
plt.axis([0, 8, 0, 15])

i=0
x=list()
y=list()
n_under = 0
draw_function(1000)

while i < 1000:
    temp_y = np.random.randint(1000)%15
    temp_x = np.random.randint(1000)%8

    x.append(i)
    if is_under(temp_x, temp_y):
        n_under += 1
        plt.scatter(temp_x, temp_y, color='r')
    else:
        plt.scatter(temp_x, temp_y, color='g')
    i+=1
    plt.show()
    plt.xlabel("{0} under: {1}, area: {2}".format(i, n_under, (n_under / float(i)) * (200)))
    plt.pause(0.0000001) #Note this correcti