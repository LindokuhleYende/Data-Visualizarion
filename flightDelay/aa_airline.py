import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filepath = "flightDelay/flight_delays.csv"
df = pd.read_csv(filepath, index_col="Month")

plt.title("The Average Delay Of AA Airline,Per month")
sns.lineplot(data=df["AA"], color="red")
plt.ylabel("The delay in minutes")
#plt.show()


total = sum(df["AA"])
average = int(total/12)
print(average)