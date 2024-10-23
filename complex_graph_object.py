import matplotlib.pyplot as plt

z = (4 - 4j)
j = 1j
n = 1000

comp_values = [j**i * z for i in range(n) ]
#print(comp_values[:4])

real_values = [i.real for i in comp_values]
imag_values = [k.imag for k in comp_values]


fig, ax = plt.subplots()
ax.grid()
ax.plot(real_values, imag_values, 'bo', markersize= 5)
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)


ax.axhline(0, c='black', linewidth= 1.1)
ax.axvline(0, c='black', linewidth= 1.1)

#ax.set_title('trying ax object graph')
ax.set_xlabel('Re')
ax.set_ylabel('Img', rotation= 0)

ax.yaxis.set_label_coords(0.51, 1.05)
ax.xaxis.set_label_coords(1.03, 0.52)

ax.annotate('', xy=(6., 0), xytext=(5.8, 0),
            arrowprops= dict(arrowstyle = '-|>', color= 'black', lw= 2 ))
ax.annotate('', xy=(0, 6.), xytext=(0, 5.8),
            arrowprops=dict(arrowstyle = '-|>', color= 'black', lw= 2 ))




plt.show()