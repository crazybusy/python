import pandas as pd

file = "FAO.csv"

data = pd.read_csv(file, encoding='ANSI')

print((data.shape))
print((data.ndim))

data['Y2012'].plot(kind='hist', bins = 100).show()
