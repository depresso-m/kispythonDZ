import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time


def dist(a1, a2, b):
    return (a1 - b[0]) ** 2 + (a2 - b[1]) ** 2


img = np.array(Image.open(r'C:\Users\chere\PycharmProjects\pythonProject2\winter1.jpg'))
WIDTH = img.shape[0]
HEIGHT = img.shape[1]
NODES = 200

leaves = np.random.randint(0, [WIDTH, HEIGHT], size=(200, 2))
start_time = time.perf_counter()

for row in range(WIDTH):
    for col in range(HEIGHT):
        d = np.array([row, col] * NODES).reshape((NODES, 2))
        close_x, close_y = leaves[np.argmin(np.linalg.norm(d - leaves, axis=1))]
        img[row, col] = img[close_x, close_y]


print(time.perf_counter() - start_time)
plt.imshow(img)
plt.show()