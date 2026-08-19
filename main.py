import pandas as pd
from urllib.parse import quote  #⬅️ [1] 'quote()' from Python's urllib.parse converts spaces to %20 and safely encodes special characters.
#
base = "https://data.cityofnewyork.us/resource/erm2-nwe9.csv"   #⬅️ SODA2 API with complete dataset.

where_clause = "created_date between '2024-01-01T00:00:00' and '2024-12-31T23:59:59' AND borough='BROOKLYN'"    #⬅️ Filter requirements.

url = f"{base}?$where={quote(where_clause)}&$limit=5000"

# data = pd.read_csv(url)
# print(data)

print("Starting request...")
data = pd.read_csv(url)
print("Done!")
print(data[data.agency == "NYPD"])



# NOTE:
# [1] It is necessary to convert spaces into %20 bcuz URLs cant contain raw spaces. They must be percent-encoded (eg, a space becomes %20).
#   - If URL's contain raw spaces, then API will not load ur requested data with filtered requirements. Error mssg will display on terminal.