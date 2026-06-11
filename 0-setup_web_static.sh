#!/bin/bash
# Script to set up web servers for web_static deployment

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    apt-get update
    apt-get install -y nginx
fi

# Create necessary directories
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

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

# Remove existing symbolic link if it exists
rm -f /data/web_static/current

# Create new symbolic link
ln -s /data/web_static/releases/test/ /data/web_static/current

# Change ownership of /data/ folder to ubuntu:ubuntu
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"

# Check if the configuration already has the hbnb_static location
if ! grep -q "location /hbnb_static" "$nginx_config"; then
    # Find the server block and add the new location before the closing brace
    sed -i '/server_name _;/a\
\
\tlocation /hbnb_static {\
\t\talias /data/web_static/current/;\
\t}' "$nginx_config"
fi

# Test nginx configuration
nginx -t

# Restart Nginx
systemctl restart nginx

# Exit successfully
exit 0
