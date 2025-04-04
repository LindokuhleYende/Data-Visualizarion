import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


filepath = "flightDelay/flight_delays.csv"

flight_data = pd.read_csv(filepath, index_col="Month")
print(flight_data)

plt.figure(figsize=(14,7))
plt.title("Average Arrival Delay for Each Airline, by Month")
# Heatmap showing average arrival delay for each airline by month
sns.heatmap(data=flight_data, annot=True)
plt.xlabel("Airline")
plt.show()