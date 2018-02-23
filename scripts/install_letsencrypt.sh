#!/usr/bin/env bash

apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:certbot/certbot
apt-get update
apt install -y certbot
