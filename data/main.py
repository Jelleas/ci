import pandas as pd

df = pd.read_csv("car.tsv", delimiter="\t")

df.plot(x='lat', y='long', style='o')
