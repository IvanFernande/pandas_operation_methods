import pandas as pd
import numpy as np
import timeit

# Example DataFrame
df = pd.DataFrame({'A': np.random.randint(1, 100, 10000),
                   'B': np.random.randint(1, 100, 10000)})

# Vectorization
def vectorization():
    df['C'] = df['A'] + df['B']

# iterrows()
def iterrows():
    for index, row in df.iterrows():
        df.at[index, 'C'] = row['A'] + row['B']

# apply()
def apply():
    df['C'] = df.apply(lambda row: row['A'] + row['B'], axis=1)

# Measure execution time
    # The variable number indicates the number of times each function has been executed.
vectorized_time = timeit.timeit(vectorization, number=10)
iterrows_time = timeit.timeit(iterrows, number=10)
apply_time = timeit.timeit(apply, number=10)

print(f"Vectorization: {vectorized_time}s")
print(f"Iterrows: {iterrows_time}s")
print(f"Apply: {apply_time}s")