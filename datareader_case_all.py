from math import exp, log10 
import os
import numpy as np
from matplotlib.pyplot import *

#os.system("g++ main.cpp planet.h planet.cpp")
#os.system("./a.out %d %d" % (n, t_max)) 

infile = open('positions.xyz', 'r')
t_max = 25

x_earth = []
y_earth = []
x_sun = []
y_sun = []
x_venus = []
y_venus = []
x_mercury = []
y_mercury = []
x_mars = []
y_mars = []
x_jupiter = []
y_jupiter = []
x_saturn = []
y_saturn = []
x_uranus = []
y_uranus = []
x_neptune = []
y_neptune = []
x_pluto = []
y_pluto = []

for line in infile:
    
    if line == ' ':
        break
    else:
        
        value = line.split()
        x_earth.append(float(value[0]))
        y_earth.append(float(value[1]))
        x_sun.append(float(value[3]))
        y_sun.append(float(value[4]))
        x_venus.append(float(value[6]))
        y_venus.append(float(value[7]))
        x_mercury.append(float(value[9]))
        y_mercury.append(float(value[10]))
        x_mars.append(float(value[12]))
        y_mars.append(float(value[13]))
        x_jupiter.append(float(value[15]))
        y_jupiter.append(float(value[16]))
        x_saturn.append(float(value[18]))
        y_saturn.append(float(value[19]))
        x_uranus.append(float(value[21]))
        y_uranus.append(float(value[22]))
        x_neptune.append(float(value[24]))
        y_neptune.append(float(value[25]))
        x_pluto.append(float(value[27]))
        y_pluto.append(float(value[28]))

infile.close()

plot(x_earth, y_earth)
hold("on")
plot(x_sun, y_sun)
plot(x_venus, y_venus)
plot(x_mercury, y_mercury)
plot(x_mars, y_mars)
plot(x_jupiter, y_jupiter)
plot(x_saturn, y_saturn)
plot(x_uranus, y_uranus)
plot(x_neptune, y_neptune)
plot(x_pluto, y_pluto)

title("Simulation of the solar system for %d years" % (t_max))
#axis([-35, 45, -35, 45])
#axis([-0.001, 0.02, -0.01, 0.02])

#legend(("Sun", "Earth"), loc='upper right')
#legend(("Earth", "Sun", "Venus", "Mercury", "Mars"), loc='upper right')
legend(("Sun", "Earth", "Venus", "Mercury", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"), loc='upper right')

xlabel("x-axes")
ylabel("y-axes")
show()
