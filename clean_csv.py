import pandas as pd
from filter import replace_string
import csv

df = pd.read_csv('l.csv',index_col=0)

df['text'] = df['text'].apply(replace_string)
df = df.set_index((df.index.astype(int)))
#df['id']   = df['id'].to_numeric()
df.to_csv('tweets.csv',quoting=csv.QUOTE_NONNUMERIC)