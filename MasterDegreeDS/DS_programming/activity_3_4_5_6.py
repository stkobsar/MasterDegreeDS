import pandas as pd
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

json_data = "https://data.nasa.gov/resource/y77d-th95.json"
df_nasa = pd.read_json(json_data)

df_nasa = df_nasa["year"].dropna()


#asking for print the head of the dataframe

head = pd.DataFrame.head(df_nasa)
print(head)

year_list = df_nasa.tolist()
print(year_list)
new_list_year = [ int(str(year)[:4]) for year in year_list]

#how many of them are repeated

list_repeated = [ rep for rep in new_list_year if new_list_year.count(rep) == 1]
print(len(list_repeated))

difference = max(new_list_year) - min(new_list_year)

print(difference)

