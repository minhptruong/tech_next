#!/bin/bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 336522104125.dkr.ecr.us-east-1.amazonaws.com
sudo docker build -f Dockerfile -t technext_image ..
sudo docker tag technext_image:latest 336522104125.dkr.ecr.us-east-1.amazonaws.com/technext:latest
docker push 336522104125.dkr.ecr.us-east-1.amazonaws.com/technext:latest