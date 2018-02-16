# Config docker login
mkdir -p ~/.docker
mkdir -p ~/.aws
echo '{"credsStore": "ecr-login"}' > ~/.docker/config.json

# Install docker-credential-ecr-login helper
chmod +x ~/docker-credential-ecr-login
sudo mkdir -p /opt/bin/
sudo mv ~/docker-credential-ecr-login /opt/bin/
echo export PATH=$PATH:/opt/bin > /etc/profile
