#Exercise 5.4: The diffraction limit of a telescope
from numpy import cos, sin, sqrt, pi, meshgrid, linspace, zeros
import matplotlib.pyplot as plt

def J(m,x): #Bessel's function
    def f(theta):
        return 1/pi*cos(m*theta-x*sin(theta))
    #SIMPSON'S METHOD:
    N = 1000 # number of divisions
    a = 0.0 # lower limit
    b = pi  # upper limit
    h = (b-a)/N # size of divisions
    s = 1/3*(f(a) + f(b))
    for k in range(1,N,2): # odd terms
        s += 1/3*(4*f(a+k*h))
    for k in range(2,N,2): # even terms
        s += 1/3*(2*f(a+k*h))
    return h*s

x = linspace(0,20,100)
plt.title("Bessel's functions")
plt.xlabel('x')
plt.ylabel('Jm(x)')
plt.grid(True)
plt.plot(x,J(0,x),'b-',label='J0(x)')
plt.plot(x,J(1,x),'r-',label='J1(x)')
plt.plot(x,J(2,x),'g-',label='J2(x)')
plt.legend()
plt.show()

#INTENSITY AS FUNCTION OF RADIUS
def I(r):
    k = 2*pi/0.5 # wave number
    return (J(1,k*r)/(k*r))**2

N = 1000 #precision
matrix = zeros((N,N))

x = y = linspace(-1.0, 1.0, N)
X, Y = meshgrid(x, y)
R = sqrt(X*X+Y*Y)

plt.title("Diffraction pattern")
plt.xlabel('x')
plt.ylabel('y')
plt.imshow(I(R),vmax=0.01)
plt.hot()
plt.show()
