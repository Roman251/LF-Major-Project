import pickle

# log ml-model metrices
import mlflow.sklearn
from mlflow.tracking import MlflowClient

from sklearn.metrics import classification_report

def print_auto_logged_info(r) -> None:
    tags = {k: v for k, v in r.data.tags.items() if not k.startswith("mlflow.")}
    artifacts = [f.path for f in MlflowClient().list_artifacts(r.info.run_id, "model")]
    print("run_id: {}".format(r.info.run_id))
    print("artifacts: {}".format(artifacts))
    print("params: {}".format(r.data.params))
    print("metrics: {}".format(r.data.metrics))
    print("tags: {}".format(tags))

def ml_flow(X_train, X_test, y_train, y_test, classifier, model_name:str='ml-model') -> None:
    mlflow.autolog()
    model = classifier()
    with mlflow.start_run() as run:
        model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print(classification_report(y_test, y_pred))
    print_auto_logged_info(mlflow.get_run(run_id=run.info.run_id))

    pickle.dump(model, open('../serialized_files/pickle/{}.pkl'.format(model_name),'wb'))
    
    