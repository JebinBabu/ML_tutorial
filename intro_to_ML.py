import pandas as pd

df = pd.read_csv('./datasets/iris/iris.data')

print(df.describe())