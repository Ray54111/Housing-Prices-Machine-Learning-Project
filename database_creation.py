#DATABASE CREATION
#import pandas
import pandas as pd
#import create_engine
from sqlalchemy import create_engine

#connect to PostgresSQL
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres', isolation_level='AUTOCOMMIT')

#disable autocommit mode
with engine.connect() as conn:
    conn.execute("COMMIT")
    conn.execute("DROP DATABASE IF EXISTS housing_prices")
    database_name = 'housing_prices'
    conn.execute(f"CREATE DATABASE {database_name}")

#connect to PostgresSQL database
engine = create_engine(f'postgresql://postgres:postgres@localhost:5432/housing_prices')

#create pandas dataframe
all_data = pd.read_csv("housing_prices_data.csv")

#put column names in a list
columns = list(all_data.columns)
#create an empty list
data_types = []
#look through the list
for col in columns:
    #all date columns start with "20", set to float
    if "20" in col: 
        data_types.append(f'"{col}" float')
    #set RegionID and BedroomCount columns to integer
    elif col == "RegionID" or col == "BedroomCount":
        data_types.append(f"{col} int")
    #set all other columns to varchar
    else:
        data_types.append(f"{col} varchar")
#store in a comma separated list
all_columns = ", ".join(data_types)

# drop housing table if it exists
drop_housing = "DROP TABLE IF EXISTS housing CASCADE;"
#execute the DROP TABLE statement
with engine.connect() as conn:
    conn.execute(drop_housing)
    
# create housing table with the column names from the list
housing_table = f"CREATE TABLE housing ({all_columns});"
#execute the CREATE TABLE statement
with engine.connect() as conn:
    conn.execute(housing_table)
    #import data into housing table
    all_data.to_sql("housing", engine, if_exists="replace", index=False, method="multi")

#create pandas dataframe
neighborhood_data = pd.read_csv("neighborhoods.csv")

#put column names in a list
columns = list(neighborhood_data.columns)
#create an empty list
data_types = []
#look through the list
for col in columns:
    #all date columns start with "20", set to float
    if "20" in col:
        data_types.append(f'"{col}" float')
    #set RegionID to integer
    elif col == "RegionID":
        data_types.append(f"{col} int")
    #set all other columns to varchar
    else:
        data_types.append(f"{col} varchar")
#store in a comma separated list
neighborhood_columns = ", ".join(data_types)

#drop neighborhoods table if it exists
drop_neighborhoods = "DROP TABLE IF EXISTS neighborhoods CASCADE;"
#execute the DROP TABLE statement
with engine.connect() as conn:
    conn.execute(drop_neighborhoods)

#create neighborhood table
neighborhood_table = f"CREATE TABLE neighborhoods ({neighborhood_columns})"

#execute the CREATE TABLE statement
with engine.connect() as conn:
    conn.execute(neighborhood_table)
    #import data into neighborhoods table
    neighborhood_data.to_sql("neighborhoods", engine, if_exists="replace", index=False, method="multi")

#create pandas dataframe
bedroom_data = pd.read_csv("bedrooms.csv")

#put column names in a list
columns = list(bedroom_data.columns)
#create an empty list
data_types = []
#look through the list
for col in columns:
    #set BedroomCount to integer
    if col == "BedroomCount":
        data_types.append(f"{col} int")
    #all other columns will be the date columns, set to float
    else:
        data_types.append(f'"{col}" float')
#store in a comma separated list
bedroom_columns = ", ".join(data_types)

#drop bedrooms table if it exists
drop_bedrooms = "DROP TABLE IF EXISTS bedrooms CASCADE;"
#execute the DROP TABLE statement
with engine.connect() as conn:
    conn.execute(drop_bedrooms)

#create bedroom table
bedroom_table = f"CREATE TABLE bedrooms ({bedroom_columns})"

#execute the CREATE TABLE statement
with engine.connect() as conn:
    conn.execute(bedroom_table)
    #import data into bedrooms table
    bedroom_data.to_sql("bedrooms", engine, if_exists="replace", index=False, method="multi")

#close the cursor and connection
conn.close()
