import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filepath = "medicalInsurance/insurance.csv"

insure_data = pd.read_csv(filepath)
#print(insure_data.head())


sns.scatterplot(x=insure_data['bmi'], y=insure_data['charges'], hue=insure_data['smoker'])

plt.show()