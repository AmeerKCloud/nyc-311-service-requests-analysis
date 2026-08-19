import pandas as pd
from urllib.parse import quote  #⬅️ quote() from Python's urllib.parse converts spaces to %20 and safely encodes special characters.
#
base = "https://data.cityofnewyork.us/resource/erm2-nwe9.csv"
where_clause = "created_date between '2024-01-01T00:00:00' and '2024-12-31T23:59:59' AND borough='BROOKLYN'"
url = f"{base}?$where={quote(where_clause)}&$limit=5000"
#
# data = pd.read_csv(url)
# print(data)

print("Starting request...")
data = pd.read_csv(url)
print("Done!")
print(data[data.agency == "NYPD"])