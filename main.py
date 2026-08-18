import pandas as pd
from urllib.parse import quote

base = "https://data.cityofnewyork.us/api/v3/views/erm2-nwe9/query.csv"
where_clause = "created_date between '2024-01-01T00:00:00' and '2024-12-31T23:59:59' AND borough='BROOKLYN'"
url = f"{base}?$where={quote(where_clause)}&$limit=500000"

data = pd.read_csv(url)
print(data)