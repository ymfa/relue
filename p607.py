import math, sympy
from scipy.optimize import minimize

def walk(width, theta):
  length = width * sympy.sec(theta)
  delta_y = width * sympy.tan(theta)
  return length, delta_y

def walk_time(thetas):
  y_end = math.sqrt((50**2) / 2)
  x_end = y_end + 25
  y0 = - y_end
  x0 = y0 + 25
  total_time = 0
  # the initial segment and the five marsh segments
  segments = [0, 10, 20, 30, 40, 50]
  speeds = [10, 9, 8, 7, 6, 5]
  for x1, speed, theta in zip(segments, speeds, thetas):
    length, delta_y = walk(x1 - x0, theta)
    total_time += length / speed
    y0 += delta_y
    x0 = x1
  # the final segment
  length = sympy.sqrt((x_end-x0)**2 + (y_end-y0)**2)
  total_time += length / 10
  return total_time

thetas = sympy.symbols('t0 t1 t2 t3 t4 t5')
f = sympy.lambdify(thetas, walk_time(thetas), modules='sympy')
f_helper = lambda x: f(x[0], x[1], x[2], x[3], x[4], x[5])
result = minimize(f_helper, [math.pi/4]*6)
print(result)

# visualize the path from A to B
if result.success:
  import matplotlib.pyplot as plt
  y_end = math.sqrt((50**2) / 2)
  x, y = [25 - y_end, 0, 10, 20, 30, 40, 50, 25 + y_end], [-y_end]
  for step in range(6):
    width = x[step+1] - x[step]
    y.append(width * math.tan(result.x[step]) + y[-1])
  y.append(y_end)

  fig, ax = plt.subplots()
  ax.plot(x, y, 'bo-')
  ax.text(x[0],y[0],'A',fontsize=14)
  ax.text(x[-1],y[-1],'B',fontsize=14)
  for step in range(5):
    ax.axvspan(step*10, step*10+10, alpha=step*0.1+0.1, color='red')
  plt.show()