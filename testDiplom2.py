import matplotlib.pyplot as plotter
import numpy as np
import seaborn as sns
from matplotlib import cm
import matplotlib.pyplot as plt

x = [12, 12,54, 234, 15]
xx = [12, 12,54, 234, 124]
t = [1,2,3,4,5]

hist, x1, y1 = np.histogram2d(x,t)
print(hist)
hist2, x2,y2 = np.histogram2d(xx,t)
plt.imshow(hist2)
plt.imshow(hist)

plt.show()


