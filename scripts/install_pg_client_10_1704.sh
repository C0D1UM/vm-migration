#!/usr/bin/env bash

# reference: https://gist.github.com/alistairewj/8aaea0261fe4015333ddf8bed5fe91f8
sudo add-apt-repository 'deb http://apt.postgresql.org/pub/repos/apt/ zesty-pgdg main'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
  sudo apt-key add -
sudo apt-get install postgresql-client-10
