url = "https://data.cityofnewyork.us/api/v3/views/erm2-nwe9/query.csv?$where=created_date between '2024-01-01T00:00:00' and '2024-12-31T23:59:59'&borough='BROOKLYN'&$limit=500000"" #⬅️ Currently working here.
import pandas as pd
data = pd.read_csv(url)
print(data.head())