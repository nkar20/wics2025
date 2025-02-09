# %%
import pandas as pd

# %%
df_livestock = pd.read_csv('production_livestock.csv')
df_emissions = pd.read_csv('global_emissions_1830-2023.csv')

# %%
df_emissions.columns

# %%
print(df_livestock['Area'].unique())
print(df_emissions['CNTR_NAME'].unique())

# %%
df_livestock.rename(columns = {'Area' : 'Country'}, inplace = True)
df_emissions.rename(columns = {'CNTR_NAME' : 'Country'}, inplace = True)

# %%
print(len(df_livestock['Country'].unique()))
print(len(df_emissions['Country'].unique()))

# %%
df_livestock.head()

# %%
df_livestock.columns

# %%
df_livestock = df_livestock.melt(
    id_vars = ['Country', 'Item', 'Element', 'Unit'],  # Columns to keep as-is
    value_vars = ['Y1961', 'Y1962', 'Y1963',
       'Y1964', 'Y1965', 'Y1966', 'Y1967', 'Y1968', 'Y1969', 'Y1970', 'Y1971',
       'Y1972', 'Y1973', 'Y1974', 'Y1975', 'Y1976', 'Y1977', 'Y1978', 'Y1979',
       'Y1980', 'Y1981', 'Y1982', 'Y1983', 'Y1984', 'Y1985', 'Y1986', 'Y1987',
       'Y1988', 'Y1989', 'Y1990', 'Y1991', 'Y1992', 'Y1993', 'Y1994', 'Y1995',
       'Y1996', 'Y1997', 'Y1998', 'Y1999', 'Y2000', 'Y2001', 'Y2002', 'Y2003',
       'Y2004', 'Y2005', 'Y2006', 'Y2007', 'Y2008', 'Y2009', 'Y2010', 'Y2011',
       'Y2012', 'Y2013', 'Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018', 'Y2019',
       'Y2020', 'Y2021', 'Y2022', 'Y2023'],  # Columns to "melt"
    var_name = 'Year',  # New column to label the melted variables
    value_name = 'Amount'  # New column to label the values
)
df_livestock

# %%
df_livestock['Year'] = df_livestock['Year'].str.replace('Y', '')
df_livestock['Year'] = df_livestock['Year'].astype(int)

# %%
df_livestock

# %%
countries = df_livestock['Country'].unique()
diff_countries = []
matching_countries = []
for country in df_emissions['Country'].unique():
    if country not in (countries):
        diff_countries.append(country)
    if country in countries:
        matching_countries.append(country)
print(f'Differing countries: \n{diff_countries}\n\n\
Matching countries: \n{matching_countries}')

# %%
df_emissions = df_emissions.drop(df_emissions[df_emissions['Country'].isin(
    ['ANNEXI', 'ANNEXII', 'BASIC', 'EIT', 'GLOBAL', 'Kuwaiti Oil Fires', 'LDC', 'LMDC', 'NONANNEX', 'OECD', 'EU27']
)].index)

# %%
countries = df_livestock['Country'].unique()
diff_countries = []
matching_countries = []
for country in df_emissions['Country'].unique():
    if country not in (countries):
        diff_countries.append(country)
    if country in countries:
        matching_countries.append(country)
print(f'Differing countries: \n{diff_countries}\n\n\
Matching countries: \n{matching_countries}\n\n\
Livestock countries: \n{countries}\n\n\
Emissions countries: \n{df_emissions['Country'].unique()}')

# %%
df_livestock['Country'] = df_livestock['Country'].replace({'China, Hong Kong SAR':'Hong Kong', 'China, Macao SAR':'Macao',
 'China, mainland':'China', 'China, Taiwan Province of':'Taiwan', "Democratic People's Republic of Korea": 'North Korea','Iran (Islamic Republic of)':'Iran', "Lao People's Democratic Republic":'Laos', 'Netherlands (Kingdom of the)': 'Netherlands','Republic of Korea': 'South Korea', 'Republic of Moldova':'Moldova','Russian Federation':'Russia','United Kingdom of Great Britain and Northern Ireland':'United Kingdom', 'United Republic of Tanzania': 'Tanzania','Venezuela (Bolivarian Republic of)':'Venezuela'}  )

# %%
print(len(df_livestock['Country'].unique()))
print(len(df_emissions['Country'].unique()))

# %%
countries = df_livestock['Country'].unique()
diff_countries = []
matching_countries = []
for country in df_emissions['Country'].unique():
    if country not in (countries):
        diff_countries.append(country)
    if country in countries:
        matching_countries.append(country)
print(f'Differing countries: \n{diff_countries}\n\n\
Matching countries: \n{matching_countries}\n\n\
Livestock countries: \n{countries}\n\n\
Emissions countries: \n{df_emissions['Country'].unique()}')

# %%
df_livestock_emissions = pd.merge(df_livestock,
                  df_emissions,
                  on = ['Country', 'Year'], how = 'inner')

# %%
df_livestock_emissions

# %%
df_emissions

# %%
df_emissions.drop(columns = ['ISO3', 'Unit'], inplace = True)

# %%
df_emissions

# %%
df_emissions = df_emissions.pivot(index=['Country', 'Gas', 'Year'], columns='Component', values='Data').reset_index()
df_emissions

# %%
df_livestock = df_livestock.drop(columns=['Unit', 'Element'])

# %%
df_livestock_emissions = pd.merge(df_livestock,
                  df_emissions,
                  on = ['Country', 'Year'], how = 'inner')

# %%
df_livestock_emissions

# %%
df_livestock_emissions = df_livestock_emissions[df_livestock_emissions['Gas']=='CH[4]']

# %%
df_livestock_emissions = df_livestock_emissions.drop(columns='Gas')

# %%
df_livestock_emissions

# %%
df_livestock = df_livestock.pivot(index=['Country', 'Year'], columns='Item', values='Amount').reset_index()
df_livestock

# %%
df_livestock.columns

# %%
# livestock_columns = df_livestock.columns.difference(["Country", "Year", "Asses", "Bees", "Buffalo", "Camels", "Cattle", "Chickens", "Ducks",
# "Geese", "Goats", "Horses", "Meat, Total", "Other birds", "Other camelids", "Other rodents", "Poultry Birds", "Sheep", "Swine / pigs", 
# "Turkeys"])

non_empty_counts = df_livestock.drop(columns=["Country", "Year"]).notna().sum()
non_empty_counts_df = non_empty_counts.reset_index()
non_empty_counts_df.columns = ["Column", "Non-Empty Count"]
print(non_empty_counts_df)

# %%
cols_interest_livestock = ["Country", "Year", "Cattle", "Chickens", "Goats", "Horses", "Sheep", "Swine / pigs"]
df_livestock = df_livestock[cols_interest_livestock]
df_livestock

# %%
df_livestock_emissions_new = pd.merge(df_livestock,
                  df_emissions,
                  on = ['Country', 'Year'], how = 'inner')
df_livestock_emissions_new

# %%
df_livestock_emissions_ch4 = df_livestock_emissions_new[df_livestock_emissions_new["Gas"] == "CH[4]"]
df_livestock_emissions_ch4

# %%
df_livestock_emissions_co2 = df_livestock_emissions_new[df_livestock_emissions_new["Gas"] == "CO[2]"]
df_livestock_emissions_co2

# %%
df_livestock_emissions_n2o = df_livestock_emissions_new[df_livestock_emissions_new["Gas"] == "N[2]*O"]
df_livestock_emissions_n2o

# %%
df_livestock_emissions.to_csv('livestock_emissions.csv', index = False)


