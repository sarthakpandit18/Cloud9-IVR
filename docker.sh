#!/bin/bash
cd /home/ec2-user/group19/
echo "start docker"
sudo service docker start
echo "build docker image"
#echo $PWD;ls -l
docker build --no-cache -t cloud9 .
#echo "run docker image"
#docker run -p 127.0.0.1:8000:8000 --name c1 group19

#echo "pull docker image"
#docker pull pv304053/cloud9:latest
echo "run docker image"
docker login -u pv304053 -p Pavi@1997
docker run -d -p 127.0.0.1:8000:8000 --name c1 cloud9