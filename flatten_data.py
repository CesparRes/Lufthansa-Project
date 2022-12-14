#%%
import pandas as pd
import json
import re
from pprint import pprint

# set up the list variable for the flights
data_out = []

with open("all_airports.txt", "r", encoding="utf8") as f:
    data = f.read()

#%%
## first we parse the output into a legal json format (because it arrived as a list of json dicts)
data = re.sub("}\n{", "},{", data)
data = re.sub("\['\{", "[{", data)
data = re.sub("', '", ",", data)
data = re.sub("'\]", "]", data)

#%%
## now we make it python friendly
data = json.loads(data)

#%%

## loop through the list of flight details and append just the flight departure information into our list
for i in range(len(data)):
    ## if this json entry is a list (IE the request returned more than one flight) - loop through the list and append each individually
    if type(data[i]["FlightInformation"]["Flights"]["Flight"]) == list:
        for item in data[i]["FlightInformation"]["Flights"]["Flight"]:
            data_out.append(item)
    else:
        data_out.append(data[i]["FlightInformation"]["Flights"]["Flight"])

#%%
data_out

#%%

"""## now because we have a list of json dicts again we need to parse them into a single json object
## insert commas between each entry
data_out = re.sub(r"\', \'", r",", str(data_out))

## remove the starting and trailing quotations
data_out = re.sub(r"\'\{", r"{", data_out)
data_out = re.sub(r"\}\'", r"}", data_out)
data_out = re.sub(r"\'\]", r"]", data_out)
data_out = re.sub(r",\[\{", r",{", data_out)
data_out = re.sub(r"}],", r"},", data_out)
data_out = re.sub(r"}]]", r"}]", data_out)

print(data_out)

"""


#%%
## Or dump it to json direct
with open("airports_parsed.txt", "w") as f:
    json.dump(data_out, f)
