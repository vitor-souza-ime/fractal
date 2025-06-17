import numpy as np
import matplotlib.pyplot as plt
import time

N = 1  # Profundidade/complexidade

# --- Koch Snowflake ---
def koch_snowflake(order, scale=10):
    def koch_curve(p1, p2, order):
        if order == 0:
            return [p1, p2]
        else:
            p1, p2 = np.array(p1), np.array(p2)
            delta = p2 - p1
            pA = p1 + delta / 3
            pB = p1 + delta * 2 / 3
            pC = pA + rotate60(delta / 3)
            return (
                koch_curve(p1, pA, order - 1) +
                koch_curve(pA, pC, order - 1)[1:] +
                koch_curve(pC, pB, order - 1)[1:] +
                koch_curve(pB, p2, order - 1)[1:]
            )

    def rotate60(v):
        angle = np.pi / 3
        rot = np.array([[np.cos(angle), -np.sin(angle)],
                        [np.sin(angle), np.cos(angle)]])
        return rot @ v

    p0 = np.array([0, 0])
    p1 = np.array([scale, 0])
    p2 = rotate60(p1 - p0) + p0
    pts = koch_curve(p0, p1, order)[:-1]
    pts += koch_curve(p1, p2, order)[:-1]
    pts += koch_curve(p2, p0, order)
    return np.array(pts)

# --- Mandelbrot ---
def mandelbrot(width, height, xlim, ylim, max_iter=100):
    x = np.linspace(*xlim, width)
    y = np.linspace(*ylim, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    div_time = np.zeros(Z.shape, dtype=int)

    for i in range(max_iter):
        Z = Z**2 + C
        diverge = np.abs(Z) > 2
        div_now = diverge & (div_time == 0)
        div_time[div_now] = i
        Z[diverge] = 2
    return div_time

# --- Binary Tree ---
def binary_tree(x, y, angle, depth, branch_length, lines):
    if depth == 0:
        return
    x2 = x + branch_length * np.cos(angle)
    y2 = y + branch_length * np.sin(angle)
    lines.append(((x, y), (x2, y2)))
    binary_tree(x2, y2, angle - np.pi/6, depth - 1, branch_length * 0.7, lines)
    binary_tree(x2, y2, angle + np.pi/6, depth - 1, branch_length * 0.7, lines)

# --- Dragon Curve ---
def dragon_curve(order):
    def build_sequence(order):
        seq = 'F'
        for _ in range(order):
            seq = seq + 'L' + ''.join('R' if c == 'L' else 'L' if c == 'R' else c for c in reversed(seq))
        return seq

    seq = build_sequence(order)
    dirs = {'F': (1, 0), 'L': -np.pi/2, 'R': np.pi/2}
    x, y = [0], [0]
    angle = 0

    for cmd in seq:
        if cmd == 'F':
            x.append(x[-1] + np.cos(angle))
            y.append(y[-1] + np.sin(angle))
        elif cmd in 'LR':
            angle += dirs[cmd]
    return x, y

# --- Koch ---
start = time.time()
pts = koch_snowflake(order=N)
elapsed = time.time() - start
print(f"Koch Snowflake: {elapsed:.3f} segundos")

plt.figure()
plt.plot(pts[:, 0], pts[:, 1])
plt.title(f"Koch Snowflake (N={N})")
plt.axis("equal")
plt.axis("off")
plt.show()

# --- Mandelbrot ---
start = time.time()
mandelbrot_res = 100 + N * 50
mandelbrot_iter = 50 + N * 50
img = mandelbrot(mandelbrot_res, mandelbrot_res, (-2, 1), (-1.5, 1.5), max_iter=mandelbrot_iter)
elapsed = time.time() - start
print(f"Mandelbrot Set: {elapsed:.3f} segundos")

plt.figure()
plt.imshow(img, cmap='hot', extent=(-2, 1, -1.5, 1.5))
plt.title(f"Mandelbrot Set (N={N})")
plt.axis("off")
plt.show()

# --- Binary Tree ---
start = time.time()
lines = []
binary_tree(0, -1, np.pi/2, N + 3, 0.3, lines)
elapsed = time.time() - start
print(f"Fractal Tree: {elapsed:.3f} segundos")

plt.figure()
for (x0, y0), (x1, y1) in lines:
    plt.plot([x0, x1], [y0, y1], 'g-')
plt.title(f"Fractal Tree (N={N})")
plt.axis("off")
plt.show()

# --- Dragon Curve ---
start = time.time()
x, y = dragon_curve(order=N * 2)
elapsed = time.time() - start
print(f"Dragon Curve: {elapsed:.3f} segundos")

plt.figure()
plt.plot(x, y, 'b-')
plt.title(f"Dragon Curve (N={N})")
plt.axis("equal")
plt.axis("off")
plt.show()
