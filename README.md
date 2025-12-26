# Inferential Statistics III: Probability Distributions and Statistical Inference

A comprehensive practice exercise applying inferential statistics concepts to solve real-world probability and statistical inference problems using Python.

## 📋 Overview

This repository contains a Jupyter notebook and Python script that demonstrate various probability distributions (Binomial, Uniform, Normal), sampling distributions, interval estimation, and hypothesis testing through practical examples.

## 🎯 Learning Objectives

- Apply binomial distribution to solve quality control and probability problems
- Analyze uniform distribution using real-world time data
- Utilize normal distribution for various probability calculations
- Understand sampling distributions and their applications
- Construct confidence intervals for population parameters
- Formulate and test hypotheses using statistical methods

## 📁 Repository Structure

```
.
├── README.md                                    # This file
├── Question Notebook - Practice Exercise.ipynb  # Jupyter notebook with all exercises
├── practice_exercise.py                        # Python script version
├── assignment.csv                              # Dataset: Student assignment completion times
├── PROBLEM_STATEMENT.md                        # Detailed problem statement
└── PROBLEM_STATEMENT_CONCISE.md                # Concise problem statement
```

## 📊 Dataset

The `assignment.csv` file contains:
- **Student_ID**: Unique identifier for each student
- **Time_taken**: Time taken to complete the assignment (in hours)

This dataset is used for the Uniform Distribution analysis (Q4).

## 🔧 Requirements

### Python Version
- Python 3.7 or higher

### Required Libraries

Install the required packages using:

```bash
pip install pandas numpy matplotlib seaborn scipy jupyter
```

Or using conda:

```bash
conda install pandas numpy matplotlib seaborn scipy jupyter
```

### Dependencies
- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computing
- `matplotlib` - Data visualization
- `seaborn` - Statistical data visualization
- `scipy` - Scientific computing and statistical functions

## 🚀 Getting Started

### Option 1: Jupyter Notebook

1. Clone or download this repository
2. Navigate to the repository directory
3. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
4. Open `Question Notebook - Practice Exercise.ipynb`
5. Run all cells to execute the analysis

### Option 2: Python Script

1. Navigate to the repository directory
2. Run the Python script:
   ```bash
   python practice_exercise.py
   ```

## 📚 Topics Covered

### 1. Binomial Distribution
- **Q1**: LED bulb quality control (4 parts)
- **Q2**: NBA free throw probabilities (2 parts)
- **Q3**: Employee performance ratings (4 parts)

### 2. Uniform Distribution
- **Q4**: Student assignment completion time analysis
  - Plotting the probability distribution
  - Calculating probabilities for various time intervals

### 3. Normal Distribution
- **Q5**: Cell phone billing analysis (5 parts)
- **Q6**: Coke bottle filling operations (3 parts)
- **Q7**: Soft drink bottle quality control (4 parts)

### 4. Sampling Distribution
- **Q8**: Battery lifetime analysis using Central Limit Theorem

### 5. Interval Estimation
- **Q9**: 95% confidence interval for electricity usage

### 6. Hypothesis Testing
- **Q10**: Formulating null and alternative hypotheses
- **Q11**: Calculating p-values for two-tailed tests

## 📖 Usage Examples

### Running Individual Questions

Each question is self-contained. You can run specific cells in the notebook or comment/uncomment sections in the Python script.

### Modifying Parameters

All parameters (sample sizes, probabilities, means, standard deviations) are clearly defined in the code and can be easily modified for different scenarios.

## 🎓 Educational Use

This exercise is designed for:
- Students learning inferential statistics
- Data science practitioners reviewing statistical concepts
- Anyone interested in applying probability distributions to real-world problems

## 📝 Notes

- The notebook includes detailed comments explaining each calculation
- Mathematical formulas and hints are provided where relevant
- All probability values are rounded to 4 decimal places for readability
- Visualizations are included for the uniform distribution analysis

## 🤝 Contributing

This is an educational exercise. Suggestions for improvements or additional problems are welcome!

## 📄 License

This project is provided for educational purposes.

## 👤 Author

Created as part of the Applied Data Science Program - Inferential Statistics III course.

---

**Note**: Make sure the `assignment.csv` file is in the same directory as the notebook/script when running the code.

