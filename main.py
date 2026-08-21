import pandas as pd
from urllib.parse import quote  #⬅️ [1] 'quote()' from Python's urllib.parse converts spaces to %20 and safely encodes special characters.
#
base = "https://data.cityofnewyork.us/resource/erm2-nwe9.csv"   #⬅️ SODA2 API URL of complete dataset.

where_clause = "created_date between '2024-01-01T00:00:00' and '2024-12-31T23:59:59' AND borough='BROOKLYN'"    #⬅️ Filter requirements.

url = f"{base}?$where={quote(where_clause)}&$limit=100000"    #⬅️ API + filter reqs to reduce size of massive dataset down to relevant data only.

print("Starting request...")        #⬅️ Test to ensure python script is running.
df = pd.read_csv(url)               #⬅️ Any delay in this loading can b either due 2 script or network/request issue.
print("Done!")                      #⬅️ Test to ensure python script is running.

# print(df.head())                  #⬅️ '.head()' method retrieves & displays first few rows.

# print(type(df.columns))         #⬅️ '.columns' is an attribute that returns an Index object (a special pandas data structure) containing all the column labels of the DataFrame.

# column_headings = df.columns.tolist()    #⬅️'.tolist()' converts a pandas index obj. or series data-structure into python list.

# for heading in column_headings:
#     print(heading)

# print(df[df.agency == "NYPD"])  #⬅️ Retrieves all rows containing NYPD keyword.


# print(pd.__version__)           #⬅️ Checking to see ur current pandas version.


# NOTE:
# [1] It is necessary to convert spaces into %20 bcuz URLs cant contain raw spaces. They must be percent-encoded (eg, a space becomes %20).
#   - If URL's contain raw spaces, then API will not load ur requested data with filtered requirements. Error mssg will display on terminal.

# saved to gitHub.





























