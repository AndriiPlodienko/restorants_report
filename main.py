import numpy as np
import pandas as pd
import requests

url = "https://api.yelp.com/v3/businesses/search?sort_by=best_match&limit=20"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer ofGxIDdZPE7EyXDshjmz-IuStboHq9jOw7iEhZGKzIyrWgmFfKyP-g-Fu84_DspY5pUpqOwmvNbU1XLk88z6IeYUBtjgFXcrRsywl8XXCfedGI93ecAF7UmG3xcSZHYx"
}

location = input("Input location, where you're looking for restorants:")
params ={
    "term": "restorans",
    "location": location
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

restorants = []

for businesses in data["businesses"]:
    name = businesses["name"]
    rating = businesses["rating"]
    price = businesses.get("price", "")
    address = ", ".join(businesses["location"]["display_address"])
    restorants.append([name, rating, price, address])

df = pd.DataFrame(restorants, columns=["Name", "Rating", "Price gap", "Address"])

print(df.to_string(index=False))
