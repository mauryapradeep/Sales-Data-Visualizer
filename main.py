import numpy as np

# Generate synthetic data
np.random.seed(0)  # For reproducibility

# Number of students
num_students = 100

# Scores in different subjects (Math, Science, English)
math_scores = np.random.randint(50, 101, num_students)
science_scores = np.random.randint(50, 101, num_students)
english_scores = np.random.randint(50, 101, num_students)

# Create a 2D array to hold all scores
scores = np.array([math_scores, science_scores, english_scores])

# Print the first 5 rows of scores
print("First 5 rows of scores:")
print(scores[:, :5])

# Calculate mean, median, and standard deviation for each subject
mean_scores = np.mean(scores, axis=1)
median_scores = np.median(scores, axis=1)
std_deviation = np.std(scores, axis=1)

print("\nMean scores for Math, Science, English:", mean_scores)
print("Median scores for Math, Science, English:", median_scores)
print("Standard deviation for Math, Science, English:", std_deviation)

# Find the highest and lowest scores for each subject
max_scores = np.max(scores, axis=1)
min_scores = np.min(scores, axis=1)

print("\nHighest scores for Math, Science, English:", max_scores)
print("Lowest scores for Math, Science, English:", min_scores)

# Analyze correlation between subjects
correlation_matrix = np.corrcoef(scores)
print("\nCorrelation matrix between subjects:")
print(correlation_matrix)

