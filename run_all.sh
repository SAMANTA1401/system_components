#!/bin/bash

echo "Starting backend servers..."
python backend_servers/app.py &
python backend_servers/app2.py &
python backend_servers/app3.py &

echo "Starting Nginx..."
sudo nginx -c $(pwd)/nginx/nginx.conf

echo "API available at http://localhost/greet"

# Keep the script running to allow the backend servers and nginx to continue
tail -f /dev/null