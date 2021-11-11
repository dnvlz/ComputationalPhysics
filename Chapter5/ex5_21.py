#Exercise 5.21: Electric field of a charge distribution
from numpy import pi,meshgrid,linspace,sqrt,errstate,sin
import matplotlib.pyplot as plt

def int_y(f,n):
    a = -5
    b = 5
    N = 2**(n-1)
    h = (b-a)/N
    def int_x(f,y,n): #adaptative trapezoidal rule
        N = 2**(n-1)
        h = (b-a)/N
        if n == 1:
            return 0.5*h*(f(a,y)+f(b,y))
        else:
            I = 1/2*int_x(f,y,n-1)
            for k in range(1,N,2):
                I += h*f(a+k*h,y)
            return I
    if n == 1:
        return 0.5*h*(int_x(f,a,n)+int_x(f,b,n))
    else:
        I = 1/2*int_y(f,n-1)
        for k in range(1,N,2):
            I += h*int_x(f,a+k*h,n)
        return I

def potential(x,y):
    epsilon = 8.8542E-12
    def f(x0,y0):
        def sigma(x0,y0):
            q0 = 1E-2 #C cm**-2
            L = 10 #cm
            return q0*sin(2*pi*x0/L)*sin(2*pi*y0/L)
        return sigma(x0,y0)/(sqrt((x-x0)**2+(y-y0)**2))
    with errstate(divide='ignore'):
        return  1/(4*pi*epsilon)*int_y(f,10)

size = 50
x = y = linspace(-size,size,300)
X,Y = meshgrid(x,y)
Z = potential(X,Y)

plt.title('Electric potential')
plt.xlabel('x')
plt.ylabel('y')
plt.imshow(Z,vmax=1E9,vmin=-1E9)
plt.jet()
plt.show()

def E_field(x,y):
    h = 1E-5
    def dfdx(f,x,y):
        return (f(x+h/2,y)-f(x-h/2,y))/h
    def dfdy(f,x,y):
        return (f(x,y+h/2)-f(x,y-h/2))/h
    return -dfdx(potential,x,y),-dfdy(potential,x,y)

Ex, Ey = E_field(X,Y)
Enorm = sqrt(Ex**2+Ey**2)
Ex, Ey = Ex/Enorm, Ey/Enorm


plt.title('Electric field')
plt.xlabel('x')
plt.ylabel('y')
plt.imshow(Enorm,extent=[-size,size,-size,size],vmax=1.5E9,vmin=0)
plt.streamplot(X,Y,Ex,Ey,density=1.5,linewidth=0.6)
plt.jet()
plt.show()
