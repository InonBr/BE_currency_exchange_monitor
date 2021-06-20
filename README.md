# BE_currency_exchange_monitor

Please clone the project and follow the steps in order to run the app properly.

## Environment setup
1. After cloning the app, in the terminal, enter the directory `cd BE_currency_exchange_monitor`.
2. Next, please created a new virtual Python environment using: `python3 -m venv venv`.
3. Now that we have a virtual Python environment to work with, let’s activate it:`source venv/bin/activate`
4. Install projects requirements using the file requirements.txt: `pip install -r requirements.txt`

## Docker

In order to connect MongoDB and set up Kafka, we need to set up docker.

**You may need to use sudo in order to run the next commands!**

1. Build the app:
```
docker-compose build --no-cache
```

2. run Docker file
```
docker-compose up -d
```

3. Kill running Docker containers
```
docker-compose down
```

4. List working Docker containers
```
sudo docker ps
```

## Test the app

**Make sure Docker containers are running!**

1. Enter the src directory using `cd src/`
2. Run all python files in a separate terminal: 
```
   - python3 data_processor_service.py
   - python3 alerts_monitor_service.py 
   - python3 alerts_handler_service.py
```

Thank you for your time!