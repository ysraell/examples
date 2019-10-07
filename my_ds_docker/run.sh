#!/bin/bash

#./stop_CONTAINER.sh || echo 'No container with iamge ds-iolive1:latest running.'
docker run -d -p 8888:8888 -p 8501:8501 -v `pwd`/work:/work -t my-ds:latest
echo 'Wait 5 seconds for Jupyter Notebook access...'
spleep 5
docker exec -it `docker ps |grep my-ds:latest|cut -d ' ' -f 1`  jupyter notebook list

