url = "https://data.cityofnewyork.us/api/v3/views/erm2-nwe9/query.csv" #⬅️ Currently working here.
import pandas as pd
data = pd.read_csv(url)
print(data.head())