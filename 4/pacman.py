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

def shader(x, y):
    cx, cy = 0.5, 0.5
    inside_circle = (x - cx) ** 2 + (y - cy) ** 2 < 0.09
    angle = math.atan2(y - cy, x - cx)
    mouth_open = (-math.pi / 6 < angle) * (angle < math.pi / 6) * (x > cx)
    eye = (x - 0.55) ** 2 + (y - 0.35) ** 2 < 0.005
    yellow = inside_circle * (1 - mouth_open)
    black_eye = eye
    
    # Шапка повара (белый овал выше верхней границы Pac-Man'а)
    hat = ((x - 0.5) ** 2 / 0.02 + (y - 0.2) ** 2 / 0.01) < 1
    white_hat = hat * (y < 0.25)
    
    r = yellow * (1 - black_eye) + white_hat
    g = yellow * (1 - black_eye) + white_hat
    b = white_hat
    
    return r, g, b

app(shader)
