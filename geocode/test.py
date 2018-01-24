import requests

address = "04-16-031-15W"

geocode_url = "https://www.lsdfinder.com/api/v1/yoursecretapikey/lsd/".format(address)
#geocode_url = geocode_url + "&json=1"

results = requests.get(geocode_url)

#results = results.json()
print(results)
