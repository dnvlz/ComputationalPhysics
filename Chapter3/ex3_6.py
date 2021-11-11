# Exercise 3.6: Deterministic chaos and the Feigenbaum plot
from numpy import arange
from matplotlib.pyplot import show, plot


for r in arange(1,4,0.01):
    vertical = []
    x = 0.5
    for i in range(1000):
        vertical.append(x)
        x = r*x*(1-x)
    horizontal = [r]*len(vertical)
    plot(horizontal,vertical,'k.')
show()
