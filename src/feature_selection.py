import pandas as pd

from feature_engineering import split

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif

def feature_selection(data_frame:pd.DataFrame, target_variable:str, n_features:int=5): 
    """
    select the top-5(default) features from the data for training and testing the model
    """

    X_train, X_test, y_train, y_test = split(data_frame, target_variable)

    sel_cols = SelectKBest(mutual_info_classif, k=n_features)
    sel_cols.fit(X_train, y_train)

    # X_train_cols = X_train.columns[sel_cols.get_support()]
    # X_test_cols  = X_test.columns[sel_cols.get_support()]

    X_train = X_train[X_train.columns.intersection(X_train.columns[sel_cols.get_support()])]
    X_test  = X_test[X_test.columns.intersection(X_test.columns[sel_cols.get_support()])]
    
    return X_train, X_test, y_train, y_test