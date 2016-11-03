from math import exp, log10 
import os
import numpy as np
from matplotlib.pyplot import *

#os.system("g++ main.cpp planet.h planet.cpp")
#os.system("./a.out %d %d" % (n, t_max)) 

infile = open('data.dat', 'r')
#n = int(infile.readline())

perihelionAngle = []

for line in infile:
    
    if line == ' ':
        break
    else:
        value = line.split()
        perihelionAngle.append(value[0])

Time = np.linspace(0, 440, len(perihelionAngle))


plot(Time, perihelionAngle)


title("Perihelion angle of Mercury for %d Mercury years" % (440))

xlabel("Time")
ylabel("$\Theta_p$")
show()




