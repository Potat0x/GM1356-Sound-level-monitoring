## GM1356 Sound level monitoring

Set of tools that allows:
- measure sound level
- save it into database
- explore with Grafana

Works with Benetech GM1356 sound level meter.


## Requirements
- Linux
- Python 3
- Docker
- make
- curl
- netcat


## Build and launch

Execute following commands:
```
# Build splread
make

# Start Grafana and MySQL
docker-compose up

# Init Grafana datasource and dashboard (use it only for the first launch)
./grafana_init.sh

# Start server that receives readings on port 2389 and saves it to database
python3 server.py

# Run splread in infinite loop and send readings from stdout to server
sudo ./infinity-splread.sh | nc localhost 2389
```
Then visit http://localhost:13000/?orgId=1&search=open (use default admin/admin credentials) and watch graph.


## Credits  
Core part of this project (`splread.c` and `Makefile`) is based on https://github.com/pvachon/gm1356.
