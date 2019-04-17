
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

#######################################################

from matplotlib import pyplot as plt
Li=  [1,2,3,4,5]
Be=  [5,5,2,3,4]
B=   [3,6,9,12,15]
C=   [3,6,2,10,15]

plt.stackplot(Li,Be,B,C, colors = ['r','m','b','c','k'])#li 기준, 나머지 누적

plt.show()

#######################################################

from matplotlib import pyplot as plt
Be=  [5,5,2,3,4]
Li=  [1,2,3,4,5]
plt.pie(Be,labels=Li,colors=['r','b','y','c','k'],startangle=45,shadow=True,explode=(0,0.1,0,0,0),autopct='%1.1f%%')

plt.show()
