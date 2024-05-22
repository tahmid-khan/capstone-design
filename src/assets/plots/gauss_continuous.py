import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

plt.rcParams["text.usetex"] = True
plt.rcParams["font.size"] = 26
plt.figure(figsize=(10, 8))

# Generate data for the normal distribution
x = np.linspace(-7, 7, 1024)
y = norm.pdf(x / 3)

# Plot the normal distribution
plt.plot(x, y, color="blue")

# Fill the area under the curve
plt.fill_between(x, y, color="blue")

# Set labels and title
plt.xticks([])  # remove x ticks and x tick labels
plt.yticks([])  # remove y ticks and y tick labels

# remove the frame
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["bottom"].set_visible(False)
plt.gca().spines["left"].set_visible(False)

# save to file
plt.savefig("gauss_continuous.pdf", format="pdf")
