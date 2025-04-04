import pandas as pd
import seaborn as sns

filepath = "/flight_delays.csv"

flight_data = pd.read_csv(filepath, index_col="Month")
#the name of the column that will be used to index the rows is "Month"

print(flight_data)