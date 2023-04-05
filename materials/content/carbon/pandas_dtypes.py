import pandas as pd
import numpy as np

ones = np.ones(shape=5000)
types = ['object', 'float64', 'int64', 'int16', 'int8', 'bool']
df = pd.DataFrame({t: ones.astype(t) for t in types})
df.memory_usage(index=False, deep=True)
# object        160000
# float64        40000
# int64          40000
# int16          10000
# int8            5000
# bool            5000
# dtype: int64