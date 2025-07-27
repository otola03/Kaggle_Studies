# Statistical Analysis Plan for F1 Data

### 1. Independent Samples T-test: Comparing Constructor Dominance Eras
- **Research Question:** Was there a statistically significant difference in the average points scored per race between two different dominant eras? For example, the Mercedes era (2014-2020) vs. the Red Bull era (2010-2013).
- **Method:** An **independent samples t-test** can compare the means of two independent groups.
- **Hypotheses:**
    - **Null (H₀):** The mean points per race for Mercedes in their era is equal to the mean points per race for Red Bull in theirs.
    - **Alternative (H₁):** The mean points per race are not equal.

### 2. One-Sample T-test: Average Position Gain
- **Research Question:** Is the average position gain for all drivers (after removing outliers) significantly different from zero?
- **Method:** A **one-sample t-test** will determine if the sample mean of `avg_position_gain` is statistically different from a hypothesized population mean (in this case, 0).
- **Hypotheses:**
    - **Null (H₀):** The true mean position gain for all drivers is 0.
    - **Alternative (H₁):** The true mean position gain is greater than 0.

### 3. Chi-Squared Test of Independence: DNF Causes vs. Engine Era
- **Research Question:** Is there a statistically significant association between the engine era (e.g., V8 era 2006-2013 vs. V6 Hybrid era 2014-present) and the most common causes of DNF (e.g., 'Engine', 'Collision', 'Accident')?
- **Method:** The **Chi-Squared (χ²) test of independence** is used to determine if there's a significant association between two categorical variables.
- **Hypotheses:**
    - **Null (H₀):** The cause of DNF is independent of the engine era.
    - **Alternative (H₁):** The cause of DNF is dependent on the engine era.

### 4. Confidence Interval for Pole Position Finish
- **Research Question:** What is the 95% confidence interval for the average final race position for drivers who qualify on pole (`grid` = 1)?
- **Method:** Calculating a **confidence interval** provides a range of plausible values for the true population mean (the average finishing position of a pole-sitter). This can be more informative than a simple point estimate (like the sample mean).
