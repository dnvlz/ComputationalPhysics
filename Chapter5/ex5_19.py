
#Exercise 5.19: Diffraction gratings
from cmath import exp,sqrt,sin,pi
import matplotlib.pyplot as plt
from numpy import linspace,empty

#d=n*pi/alpha
slit_sep = 20 #mu m
alpha = pi/slit_sep
num_slits = 10
wavelength = 0.5 #mu m
f = 100 #cm so if x is measured in cm x*u/lambda*f is adimensional
#x in cm, u in mu m, lambda in mu m, f in cm
#x ranges from -10cm to 10cm

def q(u): #u should be measured in mu m
   return sin(alpha*u)**2

# def q(u): #u should be measured in mu m
#     beta = 1/2*alpha
#     return sin(alpha*u)**2*sin(beta*u)**2

def integrand(u,x):
    return sqrt(q(u))*exp(1j*2*pi*x*u/(wavelength*f))

def int_trapezoid(f,x,n): #adaptative trapezoidal rule
    a = -(num_slits*slit_sep)/2 #number of slits*separation of slits/2
    b = (num_slits*slit_sep)/2
    N = 2**(n-1)
    h = (b-a)/N
    if n == 1:
        return 0.5*h*(f(a,x)+f(b,x))
    else:
        I = 1/2*int_trapezoid(f,x,n-1)
        for k in range(1,N,2):
            I += h*f(a+k*h,x)
        return I

def I(x):
    return abs(int_trapezoid(integrand,x,12))**2

x_vals = linspace(-5,5,500)
I_vals = list(map(I,x_vals))

plt.title('Intensity on screen as function of distance')
plt.xlabel('x')
plt.ylabel('I(x)')
plt.plot(x_vals,I_vals)
plt.show()

I_array = empty([100, 500], float)
for k in range(100):
    I_array[k, :] = I_vals

plt.imshow(I_array,vmax=3000)
plt.gray()
plt.show()