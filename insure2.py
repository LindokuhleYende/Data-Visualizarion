import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filepath = "medicalInsurance/insurance.csv"

insure_data = pd.read_csv(filepath)
#print(insure_data.head())

#does being a smoker influence the bmi
#does it also influence the charges of insurance
#sns.scatterplot(x=insure_data['bmi'], y=insure_data['charges'], hue=insure_data['smoker'])
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insure_data)
sns.swarmplot(x=insure_data['smoker'],
              y=insure_data['charges'])
plt.title("BMI of smokers and non-smokers VS The Insurance Charges")
plt.show()