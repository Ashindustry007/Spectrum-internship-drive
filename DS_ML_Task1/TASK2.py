# -*- coding: utf-8 -*-
"""
Created on Fri May  8 22:14:06 2020

@author: ASHISH
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('student-math.csv', sep=';')


def yesno(x):
    if(x=='yes'):
        return 1
    elif(x=='no'):
        return 0
    

df['Total_grades'] = df['G1'] + df['G2'] + df['G3']
df.drop(['G1','G2','G3'], axis=1,inplace= True)

#print(df)
df['paid']=df['paid'].apply(yesno)
df['schoolsup']=df['schoolsup'].apply(yesno)
df['famsup']=df['famsup'].apply(yesno)
df['activities']=df['activities'].apply(yesno)
df['nursery']=df['nursery'].apply(yesno)
df['higher']=df['higher'].apply(yesno)
df['internet']=df['internet'].apply(yesno)
df['romantic']=df['romantic'].apply(yesno)
#print(df['paid'])
fig, ax =plt.subplots(1,2)
sns.scatterplot(x='studytime', y='Total_grades',data=df,ax=ax[0])
temp= df[['studytime','Total_grades']]
sns.boxplot(data=temp,ax=ax[1])
plt.show()

