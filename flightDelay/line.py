import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filepath = "flightDelay/flight_delays.csv"
df = pd.read_csv(filepath, index_col="Month")

plt.title("The Average Delay Of Flights,Per month")
sns.lineplot(data=df)
plt.ylabel("The delay in minutes")
plt.show()