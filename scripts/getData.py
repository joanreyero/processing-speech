import pandas as pd

df = pd.read_fwf('info.txt')

df.to_csv('log.csv')


print df.head[5]
