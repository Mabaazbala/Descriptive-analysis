import numpy as npy
import pandas as pds
mydata = pds.read_csv('E:/Data collections/CSV/Discriptive/CardioGoodFitness.csv')
mydata.describe(include="all")
mydata.info()
import matplotlib.pyplot as plt
%matplotlib inline

mydata.hist(figsize=(20,30))
import seaborn as sns

sns.boxplot(x="Product", y="Age", data=mydata)
pds.crosstab(mydata['Product'],mydata['Gender'])
pds.crosstab(mydata['Product'],mydata['MaritalStatus'])
sns.countplot(x="Product", hue="Gender", data=mydata)
pds.pivot_table(mydata, index=['Product', 'Gender'],
                     columns=[ 'MaritalStatus'], aggfunc=len)
pds.pivot_table(mydata,'Income', index=['Product', 'Gender'],
                     columns=[ 'MaritalStatus'])
corr = mydata.corr()
corr                     
