#!/bin/bash

docker exec -it `docker ps |grep my-intelpython:latest|cut -d ' ' -f 1`  bash
