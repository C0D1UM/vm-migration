#!/usr/bin/env bash

# Config docker login
mkdir -p ~/.docker
mkdir -p ~/.aws
echo '{"credsStore": "ecr-login"}' > ~/.docker/config.json

#you have to create file ~/.aws/credentials manually. File content will be 
# [default]
# aws_access_key_id=<your key>
# aws_secret_access_key=<your key>

# Install docker-credential-ecr-login helper
chmod +x ~/docker-credential-ecr-login
sudo mkdir -p /opt/bin/
sudo mv ~/docker-credential-ecr-login /opt/bin/
echo export PATH=$PATH:/opt/bin > /etc/profile
