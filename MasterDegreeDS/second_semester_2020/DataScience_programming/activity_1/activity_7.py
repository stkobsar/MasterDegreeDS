import pandas as pd
import re
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

json_data = "https://data.nasa.gov/resource/y77d-th95.json"
df_nasa = pd.read_json(json_data)

#Names with more than 5 characters in the dataframe

# Make a regular expression
# to accept string starting with vowel
regex = '^[aeiouAEIOU][A-Za-z0-9_]*'

names = df_nasa["name"]

valid = [name for name in names if(re.search(regex, name) and len(name) > 5 )]
#print(valid)

#names ending with vowel


regex2 = "^(?=.+)[^aeiou]*[aeiou]+$"

valid_1 = [name for name in names if(re.search(regex2, name))]

print(valid_1)