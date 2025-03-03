import tkinter as tk
from math import sin, cos, floor
from numba import njit

@njit
def pyshader(f, w, h, t):
    scr = [0, 0, 0] * w * h
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [
                max(min(int(c * 255), 255), 0)
                for c in f(x / w, y / h, t)]
    return scr

def update(t, label, root, f):
    h = bytes('P6\n256 256\n255\n', 'ascii')
    h += bytes(pyshader(f, 256, 256, t))
    img = tk.PhotoImage(data=h).zoom(2, 2)
    label.config(image=img)
    label.image = img
    root.after(10, update, t+2, label, root, f)

def app(func):
    root = tk.Tk()
    label = tk.Label(root)
    label.pack()
    update(0, label, root, func)
    root.mainloop()

@njit
def lerp(a, b, t):
    return (1 - t) * a + t * b

@njit
def smooth(x):
    return x * x * (3 - 2 * x)

@njit
def fract(x):
    return x - floor(x)

@njit
def noise(x, y):
    return fract(sin(12.9898 * x + y * 78.233) * 43758.5453123)

@njit
def val_noise(x, y):
    a = noise(floor(x), floor(y))
    b = noise(floor(x) + 1, floor(y))
    c = noise(floor(x), floor(y) + 1)
    d = noise(floor(x) + 1, floor(y) + 1)
    ab = lerp(a, b, smooth(fract(x)))
    cd = lerp(c, d, smooth(fract(x)))
    return lerp(ab, cd, smooth(fract(y)))

@njit
def fbm(x, y, time):
    value = 0.0
    amplitude = 0.5
    frequency = 1.0
    for i in range(5):
        value += amplitude * val_noise(x * frequency + sin(time * 0.05 + i), y * frequency + cos(time * 0.05 + i))
        frequency *= 2.0
        amplitude *= 0.5
    return value

@njit
def shader(x, y, time):
    dx = sin(y * 10 + time * 0.05) * 0.05
    dy = cos(x * 10 - time * 0.05) * 0.05
    v = fbm(x + dx, y + dy, time)
    return v, v, v

app(shader)