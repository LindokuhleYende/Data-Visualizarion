import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filepath = "medicalInsurance/insurance.csv"

insure_data = pd.read_csv(filepath)
#print(insure_data.head())

#does being a smoker influence the bmi
sns.swarmplot(x=insure_data['smoker'],
              y=insure_data['charges'])
plt.title("smokers and non-smokers VS The Insurance Charges")
plt.show()