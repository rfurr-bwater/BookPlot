import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from fitting_functions import *
import scipy
from collections import Counter

# Load data
data = np.loadtxt("book_data.csv",delimiter=',',dtype=str,skiprows=1)

# Numbers
reading_scores = [float(r) for r in data[:,1]]
vocab_sizes = [float(v) for v in data[:,2]]

# How many books of each genre are there?
genre_count = Counter([str(g) for g in data[:,3]])
    # Since the assignment isn't really graded, I'm trying out collections.Counter()

fig = plt.figure(figsize=(15,13)) # Define a figure
gs = fig.add_gridspec(2,1) # Define a 2x1 'array' of subplots 

# Assign each subplot to a variable
ax1 = fig.add_subplot(gs[0,0])
ax2 = fig.add_subplot(gs[1,0])

# Line of best fit
x = np.array(vocab_sizes)
y = np.array(reading_scores)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]

sns.set_theme(style='whitegrid',font_scale=1.5)

# Scatterplot with coloration
sns.scatterplot(x=x,y=y,hue=data[:,3],ax=ax1)
ax1.set(title='Vocab Size vs Reading Score',xlabel='Vocab Size (words)',ylabel='Reading Score')
# Best fit lineplot
sns.lineplot(x=x,y=linear(x,slope,intercept),ax=ax1)

sns.barplot(data=genre_count,ax=ax2,palette='rocket')
ax2.set(title="Amount of Books Per Genre",xlabel='Genre',ylabel='Amount of Books')

plt.savefig('book')