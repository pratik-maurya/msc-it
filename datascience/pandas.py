# using pandas read csv file
import pandas as pd
df = pd.read_csv("/content/titanic.csv")
df.head()
df.describe()
df.info()
df.describe(include='all')

# error handling
try:
  df = pd.read_csv("/content/sample_data/emptyfile.csv")
  print(df,"success")
except FileNotFoundError:
  print("File not found")
except pd.errors.EmptyDataError:
  print("File is empty")
except Exception as e:
  print("No Such file is available")