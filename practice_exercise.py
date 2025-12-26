"""
Inferential Statistics III: Probability Distributions and Statistical Inference Practice Exercise

This script applies inferential statistics concepts to solve real-world probability 
and statistical inference problems using Python.
"""

# ============================================================================
# Importing the necessary libraries
# ============================================================================

# Library used for data manipulation and analysis
import pandas as pd

# Library used for working with arrays
import numpy as np

# Libraries for visualization
import matplotlib.pyplot as plt
import seaborn as sns

# This library contains a large number of probability distributions as well as 
# a growing library of statistical functions
import scipy.stats as stats

# ============================================================================
# Binomial Distribution
# ============================================================================

print("=" * 80)
print("BINOMIAL DISTRIBUTION")
print("=" * 80)

# ----------------------------------------------------------------------------
# Q1. LED Bulb Manufacturing - Quality Control
# ----------------------------------------------------------------------------
print("\nQ1. LED Bulb Manufacturing - Quality Control")
print("-" * 80)

# Q1a: Probability that none of the LED bulbs are defective
# n = 10, p = 0.05 (failure rate), k = 0
prob_none_defective = stats.binom.pmf(0, n=10, p=0.05)
print(f"a) Probability that none of the LED bulbs are defective: {prob_none_defective:.4f}")

# Q1b: Probability that exactly one LED bulb is defective
# n = 10, p = 0.05, k = 1
prob_one_defective = stats.binom.pmf(1, n=10, p=0.05)
print(f"b) Probability that exactly one LED bulb is defective: {prob_one_defective:.4f}")

# Q1c: Probability that two or fewer LED bulbs are defective
# n = 10, p = 0.05, k <= 2
prob_two_or_fewer = stats.binom.cdf(2, n=10, p=0.05)
print(f"c) Probability that two or fewer LED bulbs are defective: {prob_two_or_fewer:.4f}")

# Q1d: Probability that three or more LED bulbs are defective
# P(X >= 3) = 1 - P(X <= 2)
prob_three_or_more = 1 - stats.binom.cdf(2, n=10, p=0.05)
print(f"d) Probability that three or more LED bulbs are defective: {prob_three_or_more:.4f}")

# ----------------------------------------------------------------------------
# Q2. NBA Free Throw Shots
# ----------------------------------------------------------------------------
print("\nQ2. NBA Free Throw Shots")
print("-" * 80)

# Q2a: Probability that the player will convert both shots
# n = 2, p = 0.93, k = 2
prob_both_shots = stats.binom.pmf(2, n=2, p=0.93)
print(f"a) Probability that the player will convert both shots: {prob_both_shots:.4f}")

# Q2b: Probability that the player will convert at least one shot
# P(X >= 1) = 1 - P(X = 0)
prob_at_least_one = 1 - stats.binom.pmf(0, n=2, p=0.93)
print(f"b) Probability that the player will convert at least one shot: {prob_at_least_one:.4f}")

# ----------------------------------------------------------------------------
# Q3. Sales Trainee Ratings
# ----------------------------------------------------------------------------
print("\nQ3. Sales Trainee Ratings")
print("-" * 80)

# Q3a: Two are rated as outstanding
# n = 10, p = 0.10 (outstanding), k = 2
prob_two_outstanding = stats.binom.pmf(2, n=10, p=0.10)
print(f"a) Probability that two are rated as outstanding: {prob_two_outstanding:.4f}")

# Q3b: Two or more are rated as outstanding
# P(X >= 2) = 1 - P(X <= 1)
prob_two_or_more_outstanding = 1 - stats.binom.cdf(1, n=10, p=0.10)
print(f"b) Probability that two or more are rated as outstanding: {prob_two_or_more_outstanding:.4f}")

# Q3c: Eight of the ten are rated either outstanding or excellent
# p = 0.10 + 0.75 = 0.85 (outstanding or excellent), k = 8
prob_eight_outstanding_or_excellent = stats.binom.pmf(8, n=10, p=0.85)
print(f"c) Probability that eight of the ten are rated either outstanding or excellent: {prob_eight_outstanding_or_excellent:.4f}")

# Q3d: None of the trainees are rated as unsatisfactory
# p = 0.05 (unsatisfactory), k = 0
prob_none_unsatisfactory = stats.binom.pmf(0, n=10, p=0.05)
print(f"d) Probability that none of the trainees are rated as unsatisfactory: {prob_none_unsatisfactory:.4f}")

# ============================================================================
# Uniform Distribution
# ============================================================================

print("\n" + "=" * 80)
print("UNIFORM DISTRIBUTION")
print("=" * 80)

# ----------------------------------------------------------------------------
# Q4. Student Assignment Completion Times
# ----------------------------------------------------------------------------
print("\nQ4. Student Assignment Completion Times")
print("-" * 80)

# Load the dataset
assignment = pd.read_csv('assignment.csv')
print("\nDataset loaded successfully!")
print(f"Number of records: {len(assignment)}")
print("\nFirst few rows:")
print(assignment.head())

# Plot the probability distribution (Uniform Distribution)
# Determine the parameters
a = assignment['Time_taken'].min()
b = assignment['Time_taken'].max()

# Create a range of values for plotting
x = np.linspace(a - 0.5, b + 0.5, 1000)
# Uniform PDF: f(x) = 1/(b-a) for a <= x <= b
pdf_values = stats.uniform.pdf(x, loc=a, scale=b-a)

# Plot the uniform distribution
plt.figure(figsize=(10, 6))
plt.plot(x, pdf_values, 'b-', linewidth=2, label='Uniform PDF')
plt.fill_between(x, pdf_values, alpha=0.3)
plt.xlabel('Time taken (hours)', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.title('Uniform Distribution of Time Taken to Complete Assignment', fontsize=14)
plt.axvline(a, color='r', linestyle='--', label=f'Min = {a:.2f}')
plt.axvline(b, color='r', linestyle='--', label=f'Max = {b:.2f}')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('uniform_distribution_plot.png', dpi=300, bbox_inches='tight')
print("\nPlot saved as 'uniform_distribution_plot.png'")
plt.show()

print(f"\nUniform Distribution Parameters:")
print(f"Minimum (a): {a:.2f} hours")
print(f"Maximum (b): {b:.2f} hours")
print(f"Range: {b-a:.2f} hours")

# Q4a: Probability that a randomly selected student requires at most 2.5 hours
prob_at_most_2_5 = stats.uniform.cdf(2.5, loc=a, scale=b-a)
print(f"\na) Probability that a student requires at most 2.5 hours: {prob_at_most_2_5:.4f}")

# Q4b: Probability that a randomly selected student requires at least 3 hours
# P(X >= 3) = 1 - P(X < 3)
prob_at_least_3 = 1 - stats.uniform.cdf(3, loc=a, scale=b-a)
print(f"b) Probability that a student requires at least 3 hours: {prob_at_least_3:.4f}")

# Q4c: Probability that a randomly selected student requires 1.5 to 3.5 hours
# P(1.5 <= X <= 3.5) = P(X <= 3.5) - P(X < 1.5)
prob_between = stats.uniform.cdf(3.5, loc=a, scale=b-a) - stats.uniform.cdf(1.5, loc=a, scale=b-a)
print(f"c) Probability that a student requires 1.5 to 3.5 hours: {prob_between:.4f}")

# ============================================================================
# Normal Distribution
# ============================================================================

print("\n" + "=" * 80)
print("NORMAL DISTRIBUTION")
print("=" * 80)

# ----------------------------------------------------------------------------
# Q5. Cell Phone Bills
# ----------------------------------------------------------------------------
print("\nQ5. Cell Phone Bills")
print("-" * 80)

mean_bill = 850
std_bill = 150

# Q5a: Probability that a randomly selected cell phone bill is more than Rs. 1200
prob_more_1200 = 1 - stats.norm.cdf(1200, loc=mean_bill, scale=std_bill)
print(f"a) Probability that a cell phone bill is more than Rs. 1200: {prob_more_1200:.4f}")

# Q5b: Probability that a randomly selected cell phone bill is between Rs. 750 and Rs. 1200
prob_between_750_1200 = stats.norm.cdf(1200, loc=mean_bill, scale=std_bill) - stats.norm.cdf(750, loc=mean_bill, scale=std_bill)
print(f"b) Probability that a cell phone bill is between Rs. 750 and Rs. 1200: {prob_between_750_1200:.4f}")

# Q5c: Probability that a randomly selected cell phone bill is no more than Rs. 650
prob_no_more_650 = stats.norm.cdf(650, loc=mean_bill, scale=std_bill)
print(f"c) Probability that a cell phone bill is no more than Rs. 650: {prob_no_more_650:.4f}")

# Q5d: Amount above which lies the top 15% of cell phone bills
# P(X >= M) = 0.15 => P(X < M) = 0.85
amount_top_15 = stats.norm.ppf(0.85, loc=mean_bill, scale=std_bill)
print(f"d) Amount above which lies the top 15% of cell phone bills: Rs. {amount_top_15:.2f}")

# Q5e: Amount below which lies the bottom 25% of cell phone bills
amount_bottom_25 = stats.norm.ppf(0.25, loc=mean_bill, scale=std_bill)
print(f"e) Amount below which lies the bottom 25% of cell phone bills: Rs. {amount_bottom_25:.2f}")

# ----------------------------------------------------------------------------
# Q6. Coke Bottle Filling
# ----------------------------------------------------------------------------
print("\nQ6. Coke Bottle Filling")
print("-" * 80)

mean_coke = 500
std_coke = 20

# Q6a: Probability that the bottle filled less than 480 ml
prob_less_480 = stats.norm.cdf(480, loc=mean_coke, scale=std_coke)
print(f"a) Probability that the bottle filled less than 480 ml: {prob_less_480:.4f}")

# Q6b: Probability that the bottle filled more than 520 ml
prob_more_520 = 1 - stats.norm.cdf(520, loc=mean_coke, scale=std_coke)
print(f"b) Probability that the bottle filled more than 520 ml: {prob_more_520:.4f}")

# Q6c: Probability that the bottle filled between 470 ml to 525 ml
prob_between_470_525 = stats.norm.cdf(525, loc=mean_coke, scale=std_coke) - stats.norm.cdf(470, loc=mean_coke, scale=std_coke)
print(f"c) Probability that the bottle filled between 470 ml to 525 ml: {prob_between_470_525:.4f}")

# ----------------------------------------------------------------------------
# Q7. Soft Drink Bottles
# ----------------------------------------------------------------------------
print("\nQ7. Soft Drink Bottles")
print("-" * 80)

mean_drink = 2.0
std_drink = 0.05

# Q7a: Probability that the bottle content is between 1.9 and 2.0 liters
prob_between_1_9_2_0 = stats.norm.cdf(2.0, loc=mean_drink, scale=std_drink) - stats.norm.cdf(1.9, loc=mean_drink, scale=std_drink)
print(f"a) Probability that the bottle content is between 1.9 and 2.0 liters: {prob_between_1_9_2_0:.4f}")

# Q7b: Probability that the bottle content is between 1.9 and 2.1 liters
prob_between_1_9_2_1 = stats.norm.cdf(2.1, loc=mean_drink, scale=std_drink) - stats.norm.cdf(1.9, loc=mean_drink, scale=std_drink)
print(f"b) Probability that the bottle content is between 1.9 and 2.1 liters: {prob_between_1_9_2_1:.4f}")

# Q7c: Probability that the bottle content is below 1.9 liters or above 2.1 liters
prob_below_1_9 = stats.norm.cdf(1.9, loc=mean_drink, scale=std_drink)
prob_above_2_1 = 1 - stats.norm.cdf(2.1, loc=mean_drink, scale=std_drink)
prob_below_or_above = prob_below_1_9 + prob_above_2_1
print(f"c) Probability that the bottle content is below 1.9 liters or above 2.1 liters: {prob_below_or_above:.4f}")

# Q7d: 99% of the bottles contain at least what amount of soft drink
# P(X >= M) = 0.99 => P(X < M) = 0.01
amount_99_percent = stats.norm.ppf(0.01, loc=mean_drink, scale=std_drink)
print(f"d) 99% of the bottles contain at least {amount_99_percent:.4f} liters of soft drink")

# ============================================================================
# Sampling Distribution
# ============================================================================

print("\n" + "=" * 80)
print("SAMPLING DISTRIBUTION")
print("=" * 80)

# ----------------------------------------------------------------------------
# Q8. Battery Lifetime
# ----------------------------------------------------------------------------
print("\nQ8. Battery Lifetime")
print("-" * 80)

# Probability that the mean lifetime of 40 randomly sampled batteries will be less than 58 months
# Population: mean = 60, std = 6
# Sample size n = 40
# Sampling distribution of sample mean: mean = 60, std_error = 6/sqrt(40)
pop_mean = 60
pop_std = 6
n = 40
std_error = pop_std / np.sqrt(n)

prob_mean_less_58 = stats.norm.cdf(58, loc=pop_mean, scale=std_error)
print(f"Probability that the mean lifetime of 40 randomly sampled batteries will be less than 58 months: {prob_mean_less_58:.4f}")

# ============================================================================
# Interval Estimation
# ============================================================================

print("\n" + "=" * 80)
print("INTERVAL ESTIMATION")
print("=" * 80)

# ----------------------------------------------------------------------------
# Q9. Electricity Usage
# ----------------------------------------------------------------------------
print("\nQ9. Electricity Usage - 95% Confidence Interval")
print("-" * 80)

# 95% confidence interval for the mean usage
# Sample: n = 40, x_bar = 310
# Population: std = 89 (known)
# For 95% CI: z_alpha/2 = 1.96
n_sample = 40
x_bar = 310
pop_std_known = 89
z_critical = stats.norm.ppf(0.975)  # 95% confidence level, two-tailed

# Confidence interval formula: x_bar ± z_alpha/2 * (std / sqrt(n))
margin_of_error = z_critical * (pop_std_known / np.sqrt(n_sample))
lower_bound = x_bar - margin_of_error
upper_bound = x_bar + margin_of_error

print(f"95% Confidence Interval for the mean usage:")
print(f"Lower bound: {lower_bound:.2f} kWh")
print(f"Upper bound: {upper_bound:.2f} kWh")
print(f"\nExpression: {x_bar} ± {z_critical:.2f} × ({pop_std_known} / √{n_sample})")
print(f"Or: {x_bar} ± {margin_of_error:.2f}")

# ============================================================================
# Hypothesis Testing
# ============================================================================

print("\n" + "=" * 80)
print("HYPOTHESIS TESTING")
print("=" * 80)

# ----------------------------------------------------------------------------
# Q10. Restaurant Waiting Time
# ----------------------------------------------------------------------------
print("\nQ10. Restaurant Waiting Time - Hypothesis Formulation")
print("-" * 80)

# State the null and alternative hypothesis
# H0: The waiting time has not changed from 4.5 minutes (μ = 4.5)
# H1: The waiting time has changed from 4.5 minutes (μ ≠ 4.5)

print("Null Hypothesis (H0): μ = 4.5 minutes")
print("Alternative Hypothesis (H1): μ ≠ 4.5 minutes")
print("\nThis is a two-tailed test since we want to determine if the waiting time has changed (either increased or decreased).")

# ----------------------------------------------------------------------------
# Q11. P-value Calculation
# ----------------------------------------------------------------------------
print("\nQ11. P-value Calculation")
print("-" * 80)

# Find the p-value of a two-tailed hypothesis test if Z-stat = +2.00
z_stat = 2.00

# For a two-tailed test, p-value = 2 * P(Z > |z_stat|)
# Since z_stat is positive, P(Z > 2.00) = 1 - P(Z <= 2.00)
p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
print(f"P-value for a two-tailed test with Z-stat = {z_stat}: {p_value:.4f}")
print(f"\nInterpretation: The probability of observing a test statistic as extreme as {z_stat} or more extreme, assuming the null hypothesis is true.")

# ============================================================================
# Summary
# ============================================================================

print("\n" + "=" * 80)
print("EXERCISE COMPLETED SUCCESSFULLY!")
print("=" * 80)
print("\nAll questions have been answered using appropriate statistical methods.")
print("Results are displayed above with probabilities rounded to 4 decimal places.")

