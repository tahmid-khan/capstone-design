import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

plt.rcParams["text.usetex"] = True
plt.rcParams["font.size"] = 26
plt.figure(figsize=(10, 8))

NQ = 3
RANGE_MAX = 2**NQ - 1

# Generate 2^NQ points uniformly spaced
x = np.linspace(-RANGE_MAX, RANGE_MAX, 2**NQ)

# Compute the normal distribution values at these points
y = norm.pdf(x / 3)

# Create the histogram

bars = plt.bar(x, y, width=1, color="blue", edgecolor=None)

# Add y-values at the top of each bar
for i, bar in enumerate(bars):
    pos_x = bar.get_x() + bar.get_width() / 2
    pos_y = bar.get_height() + 0.01
    text = f"$C_{{{i}}}\\kern.05pt^2$"
    plt.text(pos_x, pos_y, text, ha="center", va="bottom")

# Customize the plot

plt.yticks([])  # remove y ticks and y tick labels


def ket(n: int) -> str:
    b = bin(n)[2:].zfill(NQ)
    return f"$|\\kern.3pt {b} \\rangle$"


xlabels = [ket(i) for i in range(0, 2**NQ)]
plt.xticks(x, xlabels, rotation=60)

# remove the frame
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["bottom"].set_visible(False)
plt.gca().spines["left"].set_visible(False)

# save to file
plt.savefig("gauss_discrete.pdf", format="pdf")
