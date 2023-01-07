-------------------------------------
# download the project:
wget https://github.com/shapeandshare/anaconda.enterprise.mlflow.tracking.workflow.pruner/archive/refs/tags/0.5.1.tar.gz --output-document=assets/mlflow.tracking.pruner.0.5.1.tar.gz


# build the project:
rm -rf ./tmp
mkdir tmp
cd tmp
wget https://github.com/shapeandshare/anaconda.enterprise.mlflow.tracking.workflow.pruner/archive/refs/tags/0.5.1.tar.gz
tar xfvz 0.5.1.tar.gz
tar cfvz ../assets/mlflow.tracking.pruner.0.5.1.tar.gz anaconda.enterprise.mlflow.tracking.workflow.pruner-0.5.1/
cd ..
rm -rf ./tmp

# to deploy the project:
ae5 project upload --name "dev.mlflow.tracking.pruner" assets/mlflow.tracking.pruner.0.5.1.tar.gz

# To recreate the schedule
ae5 job create --command "MLFlowTrackingServerPruner" --schedule "0 0 * * *" --name "scheduled dev.mlflow.tracking.server pruner" "dev.mlflow.tracking.pruner" --variable MLFLOW_TRACKING_ENTITY_TTL=10 
omit of this is set at the ae5 secret level: --variable MLFLOW_TRACKING_ENTITY_TTL=10 
