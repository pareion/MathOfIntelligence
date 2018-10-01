import pandas as pd
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')



df=pd.read_csv('data.csv',delimiter=',')

xs=df['x']
ys=df['y']


