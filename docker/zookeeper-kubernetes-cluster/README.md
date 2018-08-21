Windows roll of https://github.com/AlexsJones/kubernetes-zookeeper-cluster

# install requirements
install.bat

# build environment
build_env.bat small.yaml

# create cluster
kubectl create -f deployment/