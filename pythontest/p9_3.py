import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)


matplotlib.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()
ax.plot(np.random.rand(20), '-o', ms=0, lw=0, alpha=0.7, mfc='orange')
ax.plot(10*np.random.randn(100), 10*np.random.randn(100), 'o')
ax.set_title('Using hyphen instead of Unicode minus')
fig.text(0.90, 0.05, 'Unicode minus',
         fontsize=50, color='gray',
         ha='right', va='bottom', alpha=0.5)

plt.show()
