#Exercise 6.6
from numpy import zeros,empty,arange,cos
from vpython import sphere, rate, vector, color

# Constants
N = 26
C = 1.0
m = 1.0
k = 6.0
omega = 2.0
alpha = 2*k-m*omega*omega

# Set up the initial values of the arrays
A = zeros([N,N],float)
for i in range(N-1):
    A[i,i] = alpha
    A[i,i+1] = -k
    A[i+1,i] = -k
A[0,0] = alpha - k
A[N-1,N-1] = alpha - k

v = zeros(N,float)
v[0] = C

# Perform the Gaussian elimination
for i in range(N-1):

    # Divide row i by its diagonal element
    A[i,i+1] /= A[i,i]
    v[i] /= A[i,i]

    # Now subtract it from the next row down
    A[i+1,i+1] -= A[i+1,i]*A[i,i+1]
    v[i+1] -= A[i+1,i]*v[i]

# Divide the last element of v by the last diagonal element
v[N-1] /= A[N-1,N-1]

# Backsubstitution
x = empty(N,float)
x[N-1] = v[N-1]
for i in range(N-2,-1,-1):
    x[i] = v[i] - A[i,i+1]*x[i+1]

print(x)
# Make a plot using both dots and lines
spheres = empty(N,sphere)
for n in range(N):
    spheres[n] = sphere(pos=vector(2*n-N+x[n],0,0),radius=0.2)

for t in arange(0,100,0.1):
    rate(25)
    for n in range(N):
        xt = 2*n-N+x[n]*cos(omega*t)
        spheres[n].pos = vector(xt,0,0)
