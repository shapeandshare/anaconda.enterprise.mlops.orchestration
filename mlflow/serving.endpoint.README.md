# build the project
-------------------------------------
rm mlflow.serving.endpoint.0.2.0.tar.gz
rm mlflow.serving.endpoint.0.2.1.tar.gz
rm mlflow.serving.endpoint.0.2.2.tar.gz
rm mlflow.serving.endpoint.0.2.3.tar.gz
rm -rf ./tmp
mkdir tmp
cd tmp
wget https://github.com/shapeandshare/anaconda.enterprise.mlflow.model.serving.endpoint/archive/refs/tags/0.2.3.tar.gz
tar xfvz 0.2.3.tar.gz

## Slip stream settings here

## build deployable archive
tar cfvz ../mlflow.serving.endpoint.0.2.3.tar.gz anaconda.enterprise.mlflow.model.serving.endpoint-0.2.3/
cd ..
rm -rf ./tmp

# to deploy the project:
ae5 project upload --name "dev.mlflow.endpoint.taxi" --tag "0.1.0" mlflow.serving.endpoint.0.1.0.tar.gz

# To create the deployments:
ae5 project deploy --name "dev.mlflow.endpoint.taxi" --endpoint "dev-mlflow-endpoint-taxi" --command "DevEndpoint" --private "dev.mlflow.endpoint.taxi"

# Create private deployment token
ae5 deployment token "dev.mlflow.endpoint.taxi"
