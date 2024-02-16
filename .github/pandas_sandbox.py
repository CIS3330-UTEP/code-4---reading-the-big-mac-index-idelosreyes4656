# 2/12 Pandas 

import pandas as pd 

# list_teams = ['49ers', 'chiefs', 'steelers']
# print(type(list_teams))

# series_teams = pd.Series(list_teams)
# print(series_teams)
# print(type(series_teams))


# students = {'Hawai: Isabella', 'Ohio: David','Iowa: Justin', 'Colorado: Robert'}

# print(type(students))
# print(students)

# students_series = pd.Series(index=students.keys(),data=students.values())

# print(type(students_series))
# print(students_series)

# list_teams = ['49ers', 'chiefs', 'steelers']
# print(type(list_teams))

# series_teams = pd.Series(list_teams)
# print(series_teams)
# print(type(series_teams))

# Index(['date', 'iso_a3', 'currency_code', 'name', 'local_price', 'dollar_ex',
    #    'dollar_price', 'USD_raw', 'EUR_raw', 'GBP_raw', 'JPY_raw', 'CNY_raw',
    #    'GDP_bigmac', 'adj_price', 'USD_adjusted', 'EUR_adjusted',
    #    'GBP_adjusted', 'JPY_adjusted', 'CNY_adjusted'],
    #   dtype='object')

df = pd.read_csv('big-mac-full-index.csv')
# print(type(df)) 

######to get the indexes 
# print(df.columns)
# print(type(df.columns))

# print(df)

print(df['iso_a3'])
# print(type(df['name']))



# query_text = f"iso_a3 == 'USA'"
# # create a new df
# df_usa= df.query(query_text)
# print(df_usa)

# country_code = ['USA','MEX']
# query_text = f"iso_a3 == @country_code"
# # create a new df
# df_usa= df.query(query_text)
# print(df_usa)

# country_code = ['ARG']
# query_text = f"iso_a3 == @country_code"
# # create a new df
# df_arg= df.query(query_text)
# print(round(df_arg['dollar_price'].mean(),2))

# idx_dollar_price = df_arg['dollar_price'].idxmax() 
# print(idx_dollar_price)
# arg_series = df_arg[idx_dollar_price]
# print(arg_series)
# print(type(arg_series)) 