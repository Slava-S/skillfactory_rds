#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import json

from sklearn.model_selection import KFold,cross_val_score, train_test_split


# In[2]:


def mape(y_true, y_pred):
    """оценка MEAN ABSOLUTE PERCENTAGE ERROR, которая используется в соревновании"""
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


# In[3]:


def fit_and_score_model(model, X, y):
    """Оцениваем модель и данные на трех фолдах. Выводим средюю оценку, и оценки на фолдах"""
    
    kf = KFold(n_splits=3, shuffle=True, random_state=RANDOM_STATE)
    cv_results = cross_val_score(
        model, X, y, cv=kf, n_jobs=-1, scoring=make_scorer(mape))
    
    model.fit(X,y)
    train_score = mape(y, model.predict(X))
    
    print("#"*100)
    print(model)
    print(f"train shape {X.shape}")
    print(f"cat_cols={cat_cols}")
    print(f"num_cols={num_cols}")
    print("#"*100)
    print(f"Train result: {train_score}")
    print(f'CV result: {np.mean(cv_results)} ({cv_results})')
    print("#"*100)


# In[4]:


def make_submit_file(model, X_sub, file_name='predict.csv'):
    """запишем предсказание модели в файл, готовый к отправке на kaggle"""
    predict_submission = np.exp(model.predict(X_sub))
    sample_submission = pd.read_csv('sample_submission.csv')
    sample_submission['price'] = predict_submission
    sample_submission.to_csv(file_name, index=False)
    print(sample_submission.head(10))


# In[ ]:




