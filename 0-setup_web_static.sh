#!/usr/bin/env bash

#make sure that nginx is installed

if  ! command -v  nginx > /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# these directories need to be there if not
sudo mkdir -p /data/web_static/releases/test 
sudo mkdir -p /data/web_static/shared

#a fake HTML file for testing is put there
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" | sudo tee /data/web_static/releases/test/index.html # put here

# swymbolic link done and overwrite if exists
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# owners to user and group
sudo chown -hR ubuntu:ubuntu /data/

#nginx config is updated
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# Nginx is now started
sudo service nginx restart
