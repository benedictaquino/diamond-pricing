import pandas as pd
import numpy as np

from statsmodels.stats.outliers_influence import variance_inflation_factor
from scipy.stats import levene
from sklearn.model_selection import train_test_split

def train_test_split_to_csv(filename, random_state):
    # Load dataset
    df = pd.read_csv(filename, index_col=0)

    # Train test split
    train, test = train_test_split(df, test_size = 0.25, random_state=random_state)

    # Save to csv
    train.to_csv('data/train.csv')
    test.to_csv('data/test.csv')

def data_clean(df):
    df['lnprice'] = np.log(df['price'])
    df['carat2'] = df['carat'] ** 2

    df['recolor'] = df['color']

    df['recolor'].replace(to_replace='D', value='DE', inplace=True)
    df['recolor'].replace(to_replace='E', value='DE', inplace=True)
    df['recolor'].replace(to_replace='F', value='FG', inplace=True)
    df['recolor'].replace(to_replace='G', value='FG', inplace=True)

def VIF(df):
    '''
    This function calculates the VIF for each feature.

    PARAMETERS
    ----------
    df : {pandas.DataFrame} dataframe containing features

    RETURNS
    -------
    vif_df: {pandas.DataFrame} dataframe containing VIF for each feature

    '''
    vif = {}

    for i, col in enumerate(df):
        vif[col] = variance_inflation_factor(df.values, i)

    vif_df = pd.DataFrame.from_dict(vif, orient='index', columns=['VIF'])

    return vif_df

def levenes_test(target, feature):
    '''
    This function does a Levene's Test for a categorical feature

    PARAMETERS
    ----------
    target: {pandas.Series} the response variable

    feature: {pandas.Series} the categorical feature

    RETURNS
    -------
    results: {pandas.DataFrame} dataframe containing the results of the Levene's Test
    '''
    categories = feature.unique()

    feature_dict = {category: target[feature==category] for category in categories}

    feature_tuple = (feature_dict[category] for category in categories)

    stat, pval = levene(*feature_tuple)

    results = pd.DataFrame({'Statistic': [stat], 'p-value': [pval]})

    return results
