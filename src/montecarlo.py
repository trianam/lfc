#!/usr/bin/python
import math
import numpy as np
import matplotlib.pyplot as plt
import random

numCampioni = 1000
numPuntiX = 1000

xPoints = np.linspace(-2.0, 2.0, numPuntiX) #ascisse

#plot funzione
func = lambda x: math.sin(1/x)**2

fig = plt.figure(figsize=(13, 5));
plt.xlabel('$x$')
plt.ylabel('$y$')
yPoints = list(map(func, xPoints))
plt.plot(xPoints, yPoints, label='$y=sin^2(1/x)$')
plt.legend()

#plot integrale
fig2 = plt.figure(figsize=(13, 5));
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline(0, color='green')
plt.axvline(0, color='green')

yPoints = []
for x in xPoints:  #per ogni punto delle ascisse
    #genera punti casuali e calcola se sono sotto la curva o meno
    M = 0
    N = 0
    for i in range(numCampioni):
        xi = random.uniform(0,x)
        yi = random.uniform(0,1)

        if yi < func(xi):
            M += 1
        N += 1

    integ = lambda x: (M*x)/N
    yPoints.append(integ(x))

plt.plot(xPoints, yPoints, label=r"$y\approx\int_0^x sin^2(1/x')dx'$")
plt.legend(loc=4)

plt.show()
    
