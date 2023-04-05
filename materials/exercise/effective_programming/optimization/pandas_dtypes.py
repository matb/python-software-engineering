import pandas as pd
import numpy as np

if __name__ == '__main__':

    ones = np.ones(shape=5000)
    types = ['object',float, np.float64, 'float64',int, np.int64, 'int64', 'int16', 'int8', 'bool']
    df = pd.DataFrame({t: ones.astype(t) for t in types})
    print(df.memory_usage(index=False, deep=True))