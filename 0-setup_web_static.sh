#!/usr/bin/env bash
# Creates the local web static content
apt-get update -y
apt-get install nginx -y
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\t<h1>\n\t\t\tHello World\n\t\t</h1>\n\t</body>\n</html>" > /data/web_static/releases/test/index.html
rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data
sed -i "s/server_name _;/server_name _;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}\n/g" /etc/nginx/sites-available/default
nginx -t
service nginx restart
