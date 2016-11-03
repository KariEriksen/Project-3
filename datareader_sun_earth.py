#!/usr/bin/env python
from math import exp, log10, sqrt
import os
import numpy as np
from matplotlib.pyplot import *

# Reading file data.dat, 

infile = open('positions1.xyz', 'r')

vec1 = []
vec2 = []
vec3 = []
vec4 = []
vec5 = []
vec6 = []

r = 0.0
x = 0.0
y = 0.0



for line in infile:
    
    if line == ' ':
        break
    else:

        value = line.split()
        vec1.append(float(value[0]))
        vec2.append(float(value[1]))
	x = float(value[0])
	y = float(value[1])
	r = sqrt(x*x + y*y)
        vec3.append(r)
	vec4.append(float(value[3]))
        vec5.append(float(value[4]))
        vec6.append(float(value[5]))

infile.close()

#dt = np.linspace(0, 0.001, 99999)

#t = len(dt)

years = 100


plot(vec1, vec2, 'ro')
#plot(dt, vec3)
hold("on")
plot(vec4, vec5)

#axis([-1.1, 1.1, -1.1, 1.1])
title("Simulation of Sun and Earth for %d years" % (years))

legend(("Sun", "Earth"), loc='upper right')

xlabel("x-axes")
ylabel("y-axes")
show()
