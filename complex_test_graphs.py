import math 
import numpy as np
import matplotlib.pyplot as plt   
import cmath

j = 1j

z = -j*((4 + 4j)/(2j)*(1 + j)**2)
print(z)

list_of_values = [(j**i)*z for i in range(1000)]


real_parts = [i.real for i in list_of_values]
imag_parts = [j.imag for j in list_of_values]

plt.subplots()

plt.plot(real_parts, imag_parts, 'ro', markersize= 5)
plt.xlim(-5,5);plt.ylim(-5,5)
plt.grid()
plt.axhline(0, color='black', linewidth=1.1)
plt.axvline(0, color= 'black', linewidth= 1.1)
real = 'Re'
imag = 'Img'
plt.ylabel(real)
plt.xlabel(imag)

plt.show()