import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


filepath = "flightDelay/flight_delays.csv"

flight_data = pd.read_csv(filepath, index_col="Month")
print(flight_data)