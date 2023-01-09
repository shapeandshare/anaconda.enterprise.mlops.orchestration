# download the project:
wget https://github.com/shapeandshare/anaconda.enterprise.mlflow.model.serving.endpoint/archive/refs/tags/0.3.1.tar.gz --output-document=assets/anaconda.enterprise.mlflow.model.serving.endpoint.0.3.1.tar.gz

# if splitstreaming is needed for specific builds:
rm -rf ./tmp
mkdir tmp
cd tmp
wget https://github.com/shapeandshare/anaconda.enterprise.mlflow.model.serving.endpoint/archive/refs/tags/0.3.1.tar.gz
tar xfvz 0.3.1.tar.gz
tar cfvz ../assets/anaconda.enterprise.mlflow.model.serving.endpoint.0.3.1.tar.gz anaconda.enterprise.mlflow.model.serving.endpoint-0.3.1/
cd ..
rm -rf ./tmp


# to upload the project:
ae5 project upload --name "dev.mlflow.endpoint.taxi" assets/anaconda.enterprise.mlflow.model.serving.endpoint.0.3.1.tar.gz

# To create the deployments:
ae5 project deploy --name "dev.mlflow.endpoint.taxi" --endpoint "dev-mlflow-endpoint-taxi" --command "MLFlowModelServer" --private "dev.mlflow.endpoint.taxi"
# this does not suppport deployment using variables
# --variable MLFLOW_SERVING_MODEL_NAME="taxi_fare_regressor" --variable MLFLOW_SERVING_MODEL_STAGE="Staging"

# Create private deployment token
ae5 deployment token "dev.mlflow.endpoint.taxi"
