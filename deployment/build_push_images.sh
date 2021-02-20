#!/bin/bash

set -ev # exit immediately in case of error, verbose mode
set -x # print all executed commands (=debug mode)


echo "=== Get latest docker image ==="
# login to aws ecr
docker login -u AWS -p $(aws --region us-east-2 ecr get-login-password) ${ECR_REGISTRY}

# get latest docker image for caching if available
docker pull ${ECR_REGISTRY}/${ECR_REPOSITORY}:main || true


echo "=== Build python and pyjava docker image ==="

docker build --pull=true --cache-from ${ECR_REGISTRY}/${ECR_REPOSITORY}:main \
  -t ${ECR_REGISTRY}/${ECR_REPOSITORY}:python -f Dockerfiles/Dockerfile_python .

docker build -t ${ECR_REGISTRY}/${ECR_REPOSITORY}:pyjava -f Dockerfiles/Dockerfile_pyjava \
  --build-arg ECR_REGISTRY=${ECR_REGISTRY} --build-arg ECR_REPOSITORY=${ECR_REPOSITORY} .

# to do add test script for docker image

echo "=== Push docker images to AWS ECR ==="

docker push ${ECR_REGISTRY}/${ECR_REPOSITORY}:python

docker push ${ECR_REGISTRY}/${ECR_REPOSITORY}:pyjava
