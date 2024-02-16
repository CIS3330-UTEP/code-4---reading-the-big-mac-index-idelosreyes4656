import pandas as pd

df = pd.read_csv('big-mac-full-index.csv') 

# print(df.columns)
# print(type(df.columns))
# print(len(df.columns))
# print(len(df))
# print(df.index)
# print(len(df.index))
# print(type(df.index))

# numbers = range(1631)
# print(numbers)

# for i in df.index: 
#     print(df['iso_a3'][1])
# for i in df.index: 
#     print(df['dollar_price'][1])

# for i in df.index: 
#     print(df.loc[i]['name'])

# for i in df.index: 
#     print(df.iloc[i]['name'])

#for the entire series if you dont specify row
# for i in df.index: 
#     print(df.loc[i])

# for c in df.columns: 
#     print(df.iloc[i]['name']) *******************

# for i in range(len(df)):
#     print(df.iloc[i])

# df_arg = df.query('iso_a3 == "ARG"')
# for i in range(len(df_arg)):
#     print(df_arg.iloc[i])

# for index, row in df.iterrows():
#     #print(row)
#     #print name on location
#     print(df['name'][index])

# def get_new_country_name(row):
    #print(row)
    # new_country_name = f"{row['name']} ({row['iso_a3']})"
    # print(new_country_name)
# df.apply(get_new_country_name, axis = 1) 

query_iso = f"(iso_a3 == 'ARG')"
arg_df = df.query(query_iso)
    
print(round(arg_df['dollar_price'].mean(),2))
    