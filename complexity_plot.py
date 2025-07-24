# %% Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# %%Define the first hyperbola: asymptotes y=1 and x=1
x1 = np.linspace(0.01, 0.7, 500)
y1 = -1 / (x1 - 1) + 1

# Define the second hyperbola: asymptotes y=3 and x=5
x2 = np.linspace(0.01, 1.99, 500)
y2 = -1 / (x2 - 3) + 3

# %% Create the plot
plt.figure(figsize=(6, 5))
plt.plot(x1, y1, label="Spreadsheets")
plt.plot(x2, y2, label="Programming")

# Add asymptotes for visual reference
plt.axhline(y=1, color="gray", linestyle="--", linewidth=0.5)
plt.axvline(x=0, color="gray", linestyle="--", linewidth=0.5)
plt.axhline(y=1, color="gray", linestyle="--", linewidth=0.5)
plt.axvline(x=2, color="gray", linestyle="--", linewidth=0.5)

# Customize the plot
plt.xlabel("\nComplexity")
plt.ylabel("Time to build\n")
plt.xticks([0, 1, 2], ["Simple", "Intermediate", "Sophisticated"])
plt.yticks([2, 3, 4], ["Quick", "Moderate", "Long"])
plt.legend()
plt.title("Comparison of Time to Build vs Complexity")

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()

# %%
