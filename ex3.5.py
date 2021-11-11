# Excercise 3.5:  Visualization of the solar system
from vpython import sphere, rate, vector, ring, color
from math import cos,sin,pi
from numpy import arange, array, empty

spheres = empty(7,sphere)
rings = empty(7,ring)
c1 = 2500
c2 = 100000
r_obj = array([2440,6052,6371,3386,69173,57316])*c1
r_orb = array([57.9,108.2,149.6,227.9,778.5,1433.4])*1E6
period = array([88,224.7,365.3,687,4331.6,10759.2])
omega = 2*pi/period
col = [color.magenta,color.orange,color.blue,color.red,color.orange,color.yellow,color.yellow]

for n in range(6):
    rings[n] = ring(axis=vector(0,0,1), radius=r_orb[n], thickness=0.5E6)
    spheres[n] = sphere(pos=vector(0,r_orb[n],0),radius=r_obj[n],color=col[n])

for t in arange(0,c2,0.1):
    rate(2500)
    for n in range(6):
        x = r_orb[n]*cos(omega[n]*t)
        y = r_orb[n]*sin(omega[n]*t)
        spheres[n].pos = vector(x,y,0)