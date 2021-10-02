
from log import ml_flow
from feature_engineering import load_data, scale_balance, split

# data training algorithms
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# path of training data
data_path = '../data/liver.csv'

# name the model
model_name = 'liver'

# ml-algorithm
classifier = RandomForestClassifier

if __name__=='__main__':
    data_frame = load_data(data_path)

    X_train, X_test, y_train, y_test = split(data_frame, target_variable='outcome')

    if classifier == KNeighborsClassifier:
        scaling = True
    else:
        scaling = False

    X_train, X_test, y_train, y_test = scale_balance(X_train, X_test, y_train, y_test, imbalanced=True, scaling=scaling)
    
    ml_flow(X_train, X_test, y_train, y_test, model_name=model_name, classifier=classifier)

    