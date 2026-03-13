import pandas as pd 
import numpy as np

data = {"column1" : [1, np.nan, 3, 4,],
        "column2" : [9, 10, np.nan, 2],
        "column3" : [15, 1, np.nan, np.nan],
        "category" : ['A', 'B', np.nan, 'D']}


df = pd.Dataframe(data)

print("Original dataframe")
print(df)
