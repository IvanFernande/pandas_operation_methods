# Efficiency Comparison of Data Operations in Pandas
## Introduction
**Optimizing data operations** is crucial for efficient processing of large datasets. Three common methods in Pandas are:
  1. Vectorization: Directly operating on entire arrays for efficient processing, leveraging libraries like NumPy. Highly recommended for improved performance with large datasets.
  2. Iterating with iterrows(): Involves iterating row by row through a DataFrame using a for loop, which can be less efficient compared to vectorization due to the computational cost of accessing individual rows and columns.
  3. Using apply(): Applying a function along an axis of the DataFrame, useful for complex or custom operations. However, it may be less optimal than vectorization due to the overhead of applying a function to each row or column.

**Importance of Optimization in Data Operations**:
  1. Efficiency: Enhances performance to process data quickly and effectively.
  2. Scalability: Ensures algorithms can handle growing datasets without compromising execution time.
  3. Computational Resources: Efficient utilization of computational resources is crucial for applications requiring fast and accurate processing.
  4. Productivity: Optimization reduces task time, boosting productivity in data analysis and development.

Since efficiency on very large data is crucial, I have made a brief comparison at the code level to see how it could be more optimal. For my test, I decided to create a DataFrame of a considerable size (10000 rows), and performed a sum between the two columns (which have the same size). In this way, I will be able to check which method is the most suitable by measuring the time it takes each one to perform this operation 1 time. Let's go into the code in more detail:

## Code explanation
1. We will import the libraries needed for this test.
```python
import pandas as pd
import numpy as np
import timeit
```
2. We will create the example DataFrame, with the dimensions mentioned above.

```python
df = pd.DataFrame({'A': np.random.randint(1, 100, 10000),
                   'B': np.random.randint(1, 100, 10000)})
```

3. We will include the different methods to be tested, being the ones mentioned at the beginning.

   3.1. Vectorization
   ```python
   def vectorization():
     df['C'] = df['A'] + df['B']
   ```
   3.2. Iterrows
   ```python
   def iterrows():
     for index, row in df.iterrows():
       df.at[index, 'C'] = row['A'] + row['B']
   ```
   3.3. Apply
   ```python
   def apply():
     df['C'] = df.apply(lambda row: row['A'] + row['B'], axis=1)
   ```

5. Each function will be performed once, measuring the time taken to verify which was more optimal.
```python
vectorized_time = timeit.timeit(vectorization, number=1)
iterrows_time = timeit.timeit(iterrows, number=1)
apply_time = timeit.timeit(apply, number=1)

print(f"Vectorization: {vectorized_time}s")
print(f"Iterrows: {iterrows_time}s")
print(f"Apply: {apply_time}s")
```

Then, doing a test, the results were:

   
