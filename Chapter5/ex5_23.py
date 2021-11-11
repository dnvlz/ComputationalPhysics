
#Exercise 5.23
from numpy import loadtxt,array,meshgrid,pi,arange,cos,sin,sqrt,zeros
import matplotlib.pyplot as plt

w = array(loadtxt("altitude.txt")) #altitude.txt or stm.txt

def dwdx(x,y):
    h = 30000 #30000 for altitude, 2.5 for silicon
    if x > 0 and x < (len(w[0])-1):
        return (w[y,x+1]-w[y,x-1])/(2*h)
    elif x == 0:
        return (w[y,x+1]-w[y,x])/h
    elif x == (len(w[0])-1):
        return (w[y,x]-w[y,x-1])/h

def dwdy(x,y):
    h = 30000
    if y > 0 and y < (len(w)-1):
        return (w[y+1,x]-w[y-1,x])/(2*h)
    elif y == 0:
        return (w[y+1,x]-w[y,x])/h
    elif y == (len(w)-1):
        return (w[y,x]-w[y-1,x])/h

def Intensity(x,y,phi): #phi in degrees
    return (cos(phi*pi/180)*dwdx(x,y)+sin(phi*pi/180)*dwdy(x,y))/sqrt(dwdx(x,y)**2+dwdy(x,y)**2+1)

X = len(w[0])-1
Y = len(w)-1
I = zeros([Y+1,X+1])
for x in range(X):
    for y in range(Y):
        I[y,x] = Intensity(x,y,45)

plt.title('Intensity')
plt.xlabel('x')
plt.ylabel('y')
plt.imshow(I)
plt.colorbar()
plt.bone() #jet, hot, bone, hsv, gray
plt.show()
