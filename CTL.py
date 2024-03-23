import random
import numpy as np

import random

# New mean daily time spent on LinkedIn (replace with your actual value)
new_mean_daily_time = 45      # Example: 45 minutes

# Function to simulate daily time spent (normal distribution)
def daily_linkedin_time():
    # Adjusted standard deviation remains at 10 minutes
    return random.normalvariate(new_mean_daily_time, 10)

# Sample size and number of simulations (adjust as needed)
sample_size = 1000
num_simulations = 100

# Store sample means for each simulation
sample_means = []
for _ in range(num_simulations):
    # Simulate a sample and calculate average daily time spent
    sample_time = [daily_linkedin_time() for _ in range(sample_size)]
    sample_means.append(sum(sample_time) / sample_size)

# Libraries for visualization (Matplotlib assumed)
import matplotlib.pyplot as plt

# Plot the distribution of the sample means
plt.hist(sample_means)
plt.xlabel("Average Daily Time Spent (minutes)")
plt.ylabel("Number of Simulations")
plt.title("Distribution of Average Daily LinkedIn Time (Central Limit Theorem)")
plt.show()

# Print summary statistics of the sample means
print("Average Daily Time Spent (across simulations):", sum(sample_means) / num_simulations)
print("Standard Deviation of Daily Time Spent (across simulations):", np.std(sample_means))
