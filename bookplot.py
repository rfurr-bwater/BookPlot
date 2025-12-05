import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from fitting_functions import *
import scipy

data = np.loadtxt("book_data.csv",delimiter=',',dtype=str,skiprows=1)

reading_scores = [float(r) for r in data[:,1]]
vocab_sizes = [float(v) for v in data[:,2]]

x = np.array(vocab_sizes)
y = np.array(reading_scores)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]

p = sns.scatterplot(x=x,y=y,hue=data[:,3])
p.set(title='Vocab Size vs Reading Score',xlabel='Vocab Size (words)',ylabel='Reading Score')
sns.lineplot(x=x,y=linear(x,slope,intercept))
plt.savefig('book')