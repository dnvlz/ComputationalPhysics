#Exercise 3.7: The Mandelbrot set
from numpy import linspace, zeros
from matplotlib.pyplot import imshow, show, jet

N = 2000 #grid
matrix = zeros((N,N))

i = -1
for x in linspace(-2,2,N):
    i += 1
    j = -1
    for y in linspace(-2,2,N):
        j += 1
        c = complex(x,y)
        z = complex(0,0)
        count = 0
        while (abs(z)<2):
            count += 1
            z = z*z + c
            if count == 100:
                break
        matrix[i,j] = count

imshow(matrix)
jet()
show()