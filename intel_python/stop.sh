#!/bin/bash

docker stop `docker ps |grep my-intelpython:latest|cut -d ' ' -f 1`
