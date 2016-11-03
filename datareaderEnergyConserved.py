from math import exp, log10 
import os
import numpy as np
from matplotlib.pyplot import *

#os.system("g++ main.cpp planet.h planet.cpp")
#os.system("./a.out %d %d" % (n, t_max)) 

infile = open('energy.xyz', 'r')


KineticEnergy = []
Time = []
t = 0.0

for line in infile:
    
    if line == ' ':
        break
    else:
        
        value = line.split()
	KineticEnergy.append(float(value[0]))
	t = t + 1;
	Time.append(t)
	

infile.close()

average_kinetic = sum(KineticEnergy)/(float(len(KineticEnergy)))

k = len(KineticEnergy)
DiffEnergy = []
diff = 0.0

for i in range(k):
	diff = KineticEnergy[i] - average_kinetic
	DiffEnergy.append(diff)

years = np.linspace(0, 100, 99999)


plot(years, DiffEnergy)
title("The differance in kinetic energy in system")

xlabel("Years")
ylabel("Kinetic Energy")
show()
