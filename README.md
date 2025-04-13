# Web API with Nginx Load Balancer

This project demonstrates a simple web API built with Python (Flask) and uses Nginx as a load balancer and reverse proxy.

## File Structure


## How to Run

1.  **Make the `run_all.sh` script executable:**
    ```bash
    chmod +x run_all.sh
    ```

2.  **Run the script:**
    ```bash
    ./run_all.sh
    ```

3.  **Access the API:**
    Open your web browser or use `curl` to access the API through Nginx:
    ```bash
    curl http://localhost/greet
    ```

    You should see responses coming from the different backend servers, but requests from the same IP address will consistently go to the same server due to the `ip_hash` load balancing policy.

## Explanation

* **`backend_servers/`:** Contains the Flask applications that act as our backend API instances.
* **`nginx/nginx.conf`:** The Nginx configuration file that defines the upstream backend servers and the reverse proxy/load balancing rules.
* **`run_all.sh`:** A simple script to start the backend servers and Nginx.

## Stopping the Components

To stop the backend servers and Nginx, you can:

1.  Press `Ctrl+C` in the terminal where you ran `run_all.sh`.
2.  You might need to manually stop the Nginx process using system commands (e.g., `sudo systemctl stop nginx` or `sudo service nginx stop`).