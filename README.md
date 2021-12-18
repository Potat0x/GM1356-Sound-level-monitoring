## GM1356 Sound level monitoring

Set of tools that allows:
- measure sound level
- save it into database
- explore with Grafana

Works with Benetech GM1356 sound level meter.


## Requirements
- Linux
- Python 3, mysql-connector-python
- Docker
- make
- curl
- netcat
- libhidapi-dev https://github.com/libusb/hidapi


## Build and launch

Execute following commands:
```
# Clone this repo
git clone https://github.com/Potat0x/GM1356-Sound-level-monitoring.git

cd GM1356-Sound-level-monitoring/

# Build splread
make

# Start Grafana and MySQL
docker-compose up

# Init Grafana datasource and dashboard (use it only for the first launch)
(cd grafana-init; ./init.sh)

# Start server that receives readings on port 2389 and saves it to database
python3 server/server.py

# Run splread in infinite loop and send readings from stdout to server
./splread-runner.sh
```
Then visit http://localhost:13000/?orgId=1&search=open (use default admin/admin credentials) and watch graph.


## Allow non-root users to access GM1356
For Linux Mint/Ubuntu (works also on Raspberry Pi 4):
```
cp 1337-gm1356.rules /etc/udev/rules.d/1337-gm1356.rules
```
and reconnect device.

## Launch on Raspberry PI
In `docker-compose.yml` replace `image: mysql` with `image: hypriot/rpi-mysql`.

## Credits  
Core part of this project (splread) is based on https://github.com/pvachon/gm1356.
