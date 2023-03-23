# QuickLink

QuickLink is a simple web application written in Python using the aiohttp and redis libraries. Its purpose is to allow users to shorten URLs, so they can easily share them with others, save them for later, or use them in other contexts where long URLs are not practical.

# Features
QuickLink has the following features:

* Shorten URLs: Users can input a long URL and get a short code that redirects to it.
* Redirect URLs: Users can enter a short code and be redirected to the corresponding long URL.

# Installation

To install QuickLink, follow these steps:

1. Clone the QuickLink repository from GitHub.
2. Install the required Python packages using pip: `pip install -r requirements.txt`
3. Start the Redis server.
4. Configure env variables (see Configuration section).
5. Change work directory: `cd quick_link`
6. Run the QuickLink server: `python main.py`
7. Access QuickLink in your web browser at http://localhost:8000.

# Configuration

QuickLink can be configured using environment variables. The following variables are available:

1. `REDIS_HOST`: the hostname or IP address of the Redis server
2. `REDIS_PORT`: the port number of the Redis server
3. `REDIS_PASSWORD`: the Redis password to use
4. `REDIS_USER`: the Redis user to use

# Running with Docker Compose

If you have Docker Compose installed, you can run QuickLink using the provided `docker-compose.yml` file. Follow these steps:

1. Clone the QuickLink repository from GitHub.
2. Install Docker and Docker Compose if you haven't already.
3. Start the QuickLink service using Docker Compose: `docker-compose up -d`
4. Access QuickLink in your web browser at http://localhost:8000.

Docker Compose will automatically start a Redis container and link it to the QuickLink container. 
You can customize the Redis configuration by editing the `cache` section in the `docker-compose.yml` file. 
You can also customize the QuickLink configuration by setting environment variables in the `environment` section of the `web` service.

To stop QuickLink, run `docker-compose down`. This will stop and remove the containers created by Docker Compose.

<font size="0.1">These "README.md" file generated with help of AI.</font>