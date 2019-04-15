'''
import matplotlib.pyplot as plt

x = [a for a in range(1000)]
y = [b for b in range(1000)]

x1 = [a for a in range(1000)]
y1 = [b*b for b in range(1000)]

x2 = [a + 200 for a in range(-100,100)]
y2 = [b*b*b for b in range(-100,100)]


plt.plot(x,y)
plt.plot(x1,y1)
plt.plot(x2,y2)

plt.show()
'''
