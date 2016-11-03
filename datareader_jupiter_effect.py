from math import exp, log10, sqrt
import os
import numpy as np
from matplotlib.pyplot import *

#os.system("g++ main.cpp planet.h planet.cpp")
#os.system("./a.out %d %d" % (n, t_max)) 

infile = open('positions1.xyz', 'r')

N = 10000
t = np.linspace(0, 10, 99999)
#print len(t)



r_with_jupiter = []
r_only_sun = []
x1 = []
y1 = []
r1 = 0.0
x2 = []
y2 = []
r2 = 0.0

for line in infile:
    
    if line == ' ':
        break
    else:
        
        value = line.split()
        x1 = (float(value[3]))
	y1 = (float(value[4]))
	r1 = sqrt(x1*x1+y1*y1)
	r_only_sun.append(r1)

infile.close()

    

infile = open('positions2.xyz', 'r')


for line in infile:
    
    if line == ' ':
        break
    else:
        
        value = line.split()
        x2 = (float(value[3]))
	y2 = (float(value[4]))
	r2 = sqrt(x2*x2+y2*y2)
	r_with_jupiter.append(r2)

infile.close()


plot(t, r_only_sun, 'r')
hold("on")
plot(t, r_with_jupiter, 'g')


title("How Jupiter effects the earth")

legend(("Only effected by the sun", "With effects from Jupiter"), loc='upper right')

xlabel("Time")
ylabel("Distance between Earth and Origo")
show()
