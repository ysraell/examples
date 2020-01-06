#!/bin/bash

image_name="my-intelpython:latest"

#./stop_CONTAINER.sh || echo 'No container with iamge ds-iolive1:latest running.'
docker run -d -p 8888:8888 -v $HOME:/work -t ${image_name}
echo 'Wait 5 seconds for Jupyter Notebook access...'
sleep 5
docker exec -it `docker ps |grep ${image_name}|cut -d ' ' -f 1`  jupyter notebook list
#echo -e '\nYou can now view your Streamlit app in your browser. \n\nLocal URL: http://localhost:8501\n'

