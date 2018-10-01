import pandas as pd
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')



df=pd.read_csv('data.csv',delimiter=',')

xs=df['x']
ys=df['y']

def mean_y_intercept(xs,ys):
    m=((mean(xs)*mean(ys)-mean(xs*ys))/
       (-mean(xs**2)+mean(xs)**2 ))
    b=mean(ys)-m*mean(xs)
    return m,b

m,b=mean_y_intercept(xs,ys)
print('m: '+str(m)+'& b: '+str(b))

##Graphing the data
regressionline=[m*x+b for x in xs]

plt.scatter(xs,ys)
plt.plot(xs,regressionline)
plt.show()
