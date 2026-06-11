#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx > /dev/null 2>&1; then
    apt-get update -y
    apt-get install -y nginx
fi

# Create necessary directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create fake HTML file for testing
cat > /data/web_static/releases/test/index.html << 'EOF'
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# Remove existing symbolic link and create new one
rm -f /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to ubuntu user and group recursively
chown -R ubuntu:ubuntu /data/

# Write Nginx config with hbnb_static alias location
cat > /etc/nginx/sites-available/default << 'NGINX_EOF'
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
    }

    location / {
        try_files $uri $uri/ =404;
    }
}
NGINX_EOF

# Allow HTTP traffic
ufw allow 80/tcp > /dev/null 2>&1 || true

# Restart Nginx
service nginx restart

exit 0
