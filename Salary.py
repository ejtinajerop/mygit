import pandas as pd
import os
os.listdir()
df1 = pd.read_csv('Salary_Data.csv') 
X = df1.iloc[:, :-1].values
y = df1.iloc[:, 1].values
import matplotlib.pyplot as plt
plt.scatter(X,y)
plt.title('años de experiencia vs salario')
plt.xlabel('años de experiencia')
plt.ylabel('salario')
plt.show()