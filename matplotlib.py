from matplotlib import pyplot as plt
plt.plot([1,2,3],[4,5,1])
plt.show()

x = [5,2,7]
y = [2,16,4]
plt.plot(x,y)
plt.show()

#Bargraph
from matplotlib import pyplot as plt

plt.bar([0.25,1.25,2.25],[50,40,70], label="B1",width=.5)
plt.bar([.75,1.75,2.75],[80,20,20], label="B2", color='r',width=.5)

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Test bargraph')
plt.show()

#scatter plot
from matplotlib import pyplot as plt

x = [1,1.5,2,2.5,3,3.5,3.6]
y = [7.5,8,8.5,9,9.5,10,10.5]
 
x1=[8,8.5,9,9.5,10,10.5,11]
y1=[3,3.5,3.7,4,4.5,5,5.2]
 
plt.scatter(x,y, label='+-',color='r')
plt.scatter(x1,y1,label='-+',color='b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.legend()
plt.show()
