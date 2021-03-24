# 17. GUIウィジェット

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.widgets import Cursor

# 日本語フォント設定
from matplotlib import rc
jp_font = "Yu Gothic"
rc('font', family=jp_font)

import numpy as np


x, y = 4*(np.random.rand(2, 100) - 0.5)


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, facecolor="#FFFFCC")

ax.plot(x, y, "o")
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

cursor = Cursor(ax, useblit=True, color="red", linewidth=2)

plt.show()
