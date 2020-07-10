#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
from scipy.stats import ttest_ind


# In[16]:


def about_obj(data, columns):
    for column in columns:
        data[column] = data[column].astype(str).apply(lambda x: None if x.strip() == '' else None if x.strip()=='nan' else x)
        display(data[column].value_counts())
        print("Values encountered in a column more than 10 times:", (data[column].value_counts()>10).sum())
        print("Unique values:", data[column].nunique())
        print("Missing values:", data[column].isnull().sum())
        data.loc[:,[column]].info()


# In[12]:


def about_nom(data, columns):
    for column in columns:
        data[column[0]] = data[column[0]].apply(lambda x: None if x == 'nan' else None if x>column[2] else None if x<column[1] else x)
        display(data[column[0]].value_counts())
        print("Unique values:", data[column[0]].nunique())
        print("Missing values:", data[column[0]].isnull().sum())


# In[17]:


def about_int(data, column):
    display(data[column].describe())
    data[column].hist()
    display(data[column].value_counts())
    print("Missing values:", data[column].isnull().sum())


# In[14]:


def get_boxplot(data, column):
    fig, ax = plt.subplots(figsize = (14, 4))
    sns.boxplot(x=column, y='score', data=data, ax=ax)
    plt.xticks(rotation=45)
    ax.set_title('Boxplot for ' + column)
    plt.show()


# In[15]:


def get_stat_dif(data, column):
    cols = data.loc[:, column].value_counts().index[:]
    combinations_all = list(combinations(cols, 2))
    for comb in combinations_all:
        if ttest_ind(data.loc[data.loc[:, column] == comb[0], 'score'], 
                        data.loc[data.loc[:, column] == comb[1], 'score']).pvalue \
            <= 0.05/len(combinations_all): # Bonferoni Amendment
            print('Statistically significant differences found for column', column)
            break


# In[ ]:




