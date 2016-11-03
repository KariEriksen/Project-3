from math import exp, log10 
import os
import numpy as np
from matplotlib.pyplot import *

#os.system("g++ main.cpp planet.h planet.cpp")
#os.system("./a.out %d %d" % (n, t_max)) 

infile = open('positions.xyz', 'r')
#n = int(infile.readline())
t = 100

x_earth = []
y_earth = []
x_sun = []
y_sun = []
x_jupiter = []
y_jupiter = []


for line in infile:
    
    if line == ' ':
        break
    else:
        
        value = line.split()
        x_sun.append(float(value[0]))
        y_sun.append(float(value[1]))
        x_earth.append(float(value[3]))
        y_earth.append(float(value[4]))
        x_jupiter.append(float(value[6]))
        y_jupiter.append(float(value[7]))

infile.close()
plot(x_sun, y_sun, 'r')

hold("on")
plot(x_earth, y_earth, 'b')
plot(x_jupiter, y_jupiter, 'g')


title("Simulation of the solar system for %d years" % (t))

legend(("Sun", "Earth", "Jupiter"), loc='upper right')

xlabel("x-axes")
ylabel("y-axes")
show()

