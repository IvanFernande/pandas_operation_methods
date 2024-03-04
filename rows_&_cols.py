import pandas as pd
import numpy as np
import timeit

# Generate a large DataFrame
np.random.seed(0)
df_large = pd.DataFrame(np.random.randint(1, 100, size=(100000, 3)),
columns=['A', 'B', 'C'])

# Repeat the timing experiment with this larger DataFrame
def setup_large():

    # Recreate the large DataFrame
    df_large = pd.DataFrame(np.random.randint(1, 100, size=(100000, 3)),
                            columns=['A', 'B', 'C'])

    def complex_func(row):
        if row['A'] > row['B']:
            return row['A'] + row['C']
        else:
            return row['B'] - row['C']

    return df_large, complex_func

def apply_function_large():
    df_large, complex_func = setup_large()
    df_large['D_apply'] = df_large.apply(complex_func, axis=1)

def vectorized_function_large():
    df_large, _ = setup_large()
    df_large['D_vect'] = np.where(df_large['A'] > df_large['B'],
                                  df_large['A'] + df_large['C'], df_large['B'] - df_large['C'])

# Calculate the time with timeit for the large DataFrame
time_apply_large = timeit.timeit(apply_function_large, number=1)
time_vect_large = timeit.timeit(vectorized_function_large, number=1)

print(f'Apply: {time_apply_large}s')
print(f'Vectorization: {time_vect_large}s')