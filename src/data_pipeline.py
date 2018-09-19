import pandas as pd
import numpy as np
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

    return df

if __name__ == "__main__":
    train_test_split_to_csv(filename='data/diamonds.csv', random_state=0)