import pandas as pd
from pathlib import Path

# balance imbalanced-dataset
from imblearn.over_sampling import SMOTE

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def load_data(path:str) -> pd.DataFrame:
    """
    load the data
    """
    file_path = Path(path)
    if file_path.is_file():
        data_frame = pd.read_csv(file_path)
    else:
        raise ValueError('File path error')
    
    return data_frame

def split(data_frame:pd.DataFrame, target_variable:str):
    """
    split the data into training and testing groups
    """
    X_train, X_test, y_train, y_test = train_test_split(data_frame.drop(columns=[target_variable]), data_frame[target_variable], test_size=0.2, random_state=0)
    return X_train, X_test, y_train, y_test

def scale_balance(X_train, X_test, y_train, y_test, imbalanced:bool=False, scaling:bool=False):

    """
    - balance imbalanced dataset
    - scale the dataset if required
    """

    if scaling:
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

    if imbalanced:
        smt = SMOTE(random_state=42)
        X_train, y_train = smt.fit_resample(X_train, y_train)

    return X_train, X_test, y_train, y_test