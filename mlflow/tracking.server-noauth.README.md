-------------------------------------
# Splitstream auth change:
rm -rf ./tmp
mkdir tmp
cd tmp
wget https://github.com/shapeandshare/anaconda.enterprise.mlflow.tracking.server/archive/refs/tags/0.5.0.tar.gz
tar xfvz 0.5.0.tar.gz

<update anaconda-project.yml>
<remove MLFLOW_TRACKING_TOKEN varaible>

tar cfvz ../assets/anaconda.enterprise.mlflow.tracking.server.0.5.0-no-auth.tar.gz anaconda.enterprise.mlflow.tracking.server-0.5.0/
cd ..
rm -rf ./tmp


# to upload the project:
ae5 project upload --name "dev.mlflow.tracking.server" assets/anaconda.enterprise.mlflow.tracking.server.0.5.0.tar.gz

# To create the deployment:
ae5 project deploy --name "dev.mlflow.tracking.server" --endpoint "dev-mlflow-tracking-server" --command "TrackingServer" --private "dev.mlflow.tracking.server"
These environment variables must be defined as ae5 secrets or within the anaconda-projects.yml
--variable MLFLOW_BACKEND_STORE_URI="sqlite:///data/mlflow/dev/store/mydb.sqlite" 
--variable MLFLOW_ARTIFACTS_DESTINATION="dev/mlflow/test/artifacts" 
--variable MLFLOW_TRACKING_GC_TTL="10d0h0m0s" 

Set these at the ae5 secrets or within the anaconda-
"MLFLOW_BACKEND_STORE_URI": "sqlite:///data/mlflow/dev/store/mydb.sqlite",
"MLFLOW_ARTIFACTS_DESTINATION": "data/mlflow/dev/artifacts",
"MLFLOW_TRACKING_GC_TTL": "0d0h10m0s"

# Create private deployment token
ae5 deployment token "dev.mlflow.tracking.server"

# To recreate the garbage collection schedule
ae5 job create --command "GarbageCollection" --schedule "*/10 * * * *" --name "scheduled dev.mlflow.tracking.server garbage collection" "dev.mlflow.tracking.server"
# omit if defined as ae5 secrets:
# --variable MLFLOW_BACKEND_STORE_URI="sqlite:///data/mlflow/dev/store/mydb.sqlite" --variable MLFLOW_TRACKING_GC_TTL="0d0h10m0s"
