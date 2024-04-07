#!/usr/bin/env bash
# sets up web servers for deployment of servers

sudo apt install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
sudo rm /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu: /data/
sudo sed -i "/^http {/a server {
    listen 80;
    listen [::]:80;
    server_name _;
    location /hbnb_static {
    	alias /data/web_static/current/
    }
}" /etc/nginx/nginx.conf
sudo service nginx restart
