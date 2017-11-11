import time


def fcja(x, y):
    return x + y


x = 0
y = 0

while True:
    x += 1
    y += 3
    time.sleep(5)
    print fcja(x, y)
