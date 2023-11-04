# -*- coding: utf-8 -*-
"""oibsip_taskno_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IHgq_1EhXiIH6mvAmSGeuA71vvCeeW74
"""

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/amankharwal/Website-data/master/CarPrice.csv')

df.dtypes

df.drop(columns=['car_ID'],axis=1,inplace=True)

df

import seaborn as sns
import matplotlib.pyplot as plt

len(categorical_feat)

categorical_feat

numerical_feat#remove price

len(numerical_feat)

df.corr()

plt.figure(figsize = (16,5))
ax = sns.heatmap(df.corr(), annot=True, linewidths=.1)

df[categorical_feat].head()

## Lets Find the realtionship between them and Sale PRice

for feature in categorical_feat:
    df.groupby(feature)['price'].median().plot.bar()
    plt.xlabel(feature)
    plt.ylabel('price')
    plt.title(feature)
    plt.figure(figsize=(10,10))
    plt.show()

## Lets Find the realtionship between them and Sale PRice

for feature in numerical_feat:
    df.groupby(feature)['price'].mean().plot()
    plt.xlabel(feature)
    plt.ylabel('price')
    plt.title(feature)
    plt.show()

discrete_feature=[feature for feature in numerical_feat if len(df[feature].unique())<25 and feature not in ['Id']]
print("Discrete Variables Count: {}".format(len(discrete_feature)))

discrete_feature

df[discrete_feature].head()

for feature in discrete_feature:
    df.groupby(feature)['price'].mean().plot.bar()
    plt.xlabel(feature)
    plt.ylabel('price')
    plt.title(feature)
    plt.show()

continuous_feature=[feature for feature in numerical_feat if feature not in discrete_feature]
continuous_feature

for feature in continuous_feature:
    df[feature].hist(bins=25)
    plt.xlabel(feature)
    plt.ylabel("Count")
    plt.title(feature)
    plt.show()

import numpy as np

for feature in continuous_feature:
    if 0 in df[feature].unique():
        pass
    else:
        df[feature]=np.log(df[feature])
        df['price']=np.log(df['price'])
        plt.scatter(df[feature],df['price'])
        plt.xlabel(feature)
        plt.ylabel('price')
        plt.title(feature)
        plt.show()

"""# Outliers"""

for feature in continuous_feature:
    if 0 in df[feature].unique():
        pass
    else:
        df[feature]=np.log(df[feature])
        df.boxplot(column=feature)
        plt.ylabel(feature)
        plt.title(feature)
        plt.show()

x=df[numerical_feat]
x

y = df.iloc[:,-1:]
y

from sklearn.decomposition import PCA
feat = PCA(n_components=5)
feat

feat.fit(x)

feat.components_

feat.get_feature_names_out()

feat.get_params()





df['sex']=np.where(df['sex']=="male",1,0)
df.head()
