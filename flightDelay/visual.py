import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filepath = "flightDelay/flight_delays.csv"

flight_data = pd.read_csv(filepath, index_col="Month")
#the name of the column that will be used to index the rows is "Month"

print(flight_data)

#bar chart showing the average arrival delay for 
# Spirit Airlines (airline code: NK) flights, by month

plt.figure(figsize=(10,6))
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")
# sns.barplot(x=flight_data.index, y=flight_data['NK'])
sns.barplot(data=flight_data["NK"])
plt.ylabel("Arrival delay (in minutes)")
plt.xlabel("Month")

plt.show()
