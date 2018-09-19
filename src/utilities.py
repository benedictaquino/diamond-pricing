import pandas as pd
import numpy as np

from statsmodels.stats.outliers_influence import variance_inflation_factor
from scipy.stats import levene

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

def levenes_test(df):
    '''
    This function does a Levene's Test for a categorical feature

    PARAMETERS
    ----------
    df: {pandas.DataFrame} a dataframe containing the categorical feature

    RETURNS
    -------
    results_df: {pandas.DataFrame} dataframe containing the results of the Levene's Test
    '''