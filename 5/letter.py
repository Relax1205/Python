import math
import tkinter as tk

def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr

def app(func):
    label = tk.Label()
    img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()

def box(x, y, w, h):
    x = abs(x) - w
    y = abs(y) - h
    outer = math.sqrt(max(x, 0)**2 + max(y, 0)**2)
    inner = min(0, max(x, y))
    return outer + inner

def union(a, b):
    return min(a, b)

def sdf_func(x, y):
    left = box(x + 0.2, y, 0.05, 0.3)
    right = box(x - 0.2, y, 0.05, 0.3)
    middle = box(x, y, 0.2, 0.05)
    return union(union(left, right), middle)

def shader(x, y):
    d = sdf_func(x - 0.5, y - 0.5)
    return d > 0, abs(d) * 3, 0

app(shader)
