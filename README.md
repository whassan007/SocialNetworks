## Simulating Average Daily Time Spent on LinkedIn

This project explores the Central Limit Theorem by simulating daily LinkedIn usage times and analyzing the distribution of average daily time spent across multiple simulations.

### Project Overview

The script simulates daily time spent on LinkedIn using a normal distribution with a specified mean and standard deviation. We then run multiple simulations, calculating the average daily time spent for each simulated sample. Finally, we analyze the distribution of these average times, demonstrating the Central Limit Theorem, which states that the sampling distribution of the means approaches a normal distribution regardless of the underlying population distribution (as long as the sample size is sufficiently large).

### Code Breakdown

* **`new_mean_daily_time`**: This variable stores the assumed average daily time spent on LinkedIn (in minutes). You can replace this value with your own estimate.
* **`daily_linkedin_time` function**: This function simulates a single day's LinkedIn usage time using a normal distribution with the defined mean and a standard deviation of 10 minutes (adjustable).
* **`sample_size` and `num_simulations`**: These variables define the number of users simulated per sample and the total number of simulations run, respectively. You can adjust these values based on your needs.
* **Simulation Loop**: The code iterates `num_simulations` times. In each iteration:
    * A sample of `sample_size` daily usage times is generated using `daily_linkedin_time`.
    * The average daily time spent for that sample is calculated and appended to the `sample_means` list.
* **Visualization**: The script uses Matplotlib (assumed) to create a histogram visualizing the distribution of the average daily time spent values across all simulations.
* **Summary Statistics**: The code calculates and prints the overall average daily time spent and the standard deviation of the average daily time spent across all simulations.

### Central Limit Theorem Demonstration

By running multiple simulations and observing the distribution of average daily time spent in the `sample_means` list, we expect to see a normal distribution emerge even though the underlying daily usage times follow a normal distribution. This reinforces the Central Limit Theorem principle.

### Running the Script

1. Ensure you have Python 3 and the required libraries installed (`random`, `numpy`, and `matplotlib`). 
2. Modify `new_mean_daily_time` if you want a different average daily time.
3. Adjust `sample_size` and `num_simulations` for your desired sample and simulation count.
4. Run the script using `python your_script_name.py`.

The script will generate a visualization and print summary statistics about the average daily time spent across simulations.
