import pandas as pd

url = (
    "Yhttps://officenationalstatistics-my.sharepoint.com/:x:/r/personal/"
    "george_zorinyants_ons_gov_uk/Documents/Development/data/mock_data.csv?"
    "d=w092c74d84c23476897be90cb5a16498c&csf=1&web=1&e=3tML0p"
)
df = pd.read_csv(url)
print(df.head())
