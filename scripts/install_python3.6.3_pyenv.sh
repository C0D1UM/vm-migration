#!/usr/bin/env bash

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y zlib1g-dev libssl-dev
pyenv install 3.6.3
pyenv shell 3.6.3
echo 'pyenv shell 3.6.3' >> ~/.bashrc
