from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i <= a - 10:
    j = 0
    while j <= a1 - 10:
        s = 0
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                red = arr[n][n1][0]
                green = arr[n][n1][1]
                blue = arr[n][n1][2]
                M = (int(red) + int(green) + int(blue)) // 3
                s += M
        s = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                arr[n][n1][0] = int(s // 50) * 50
                arr[n][n1][1] = int(s // 50) * 50
                arr[n][n1][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
