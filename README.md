## GM1356 Sound level monitoring

Set of tool that allows:
- measure sound level
- save it into database
- explore with Grafana

Works with Benetech GM1356 sound level meter.

## Requirements
- Linux
- Python 3
- Docker
- make


## Build and launch

```bash
# build splread
make

# start server that receives readings on port 2389 and saves it to database
python3 server.py

# run splread in infinite loop and send readings from stdout to server
sudo ./infinity-splread.sh | nc localhost 2389
```

Init database
```
docker run --rm --name spl_mysql -p 13306:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=Y mysql
docker exec -it spl_mysql bash

docker exec -it gm1356_gm1356_monitoring_db_1 bash

mysql
show databases;
create database spl_readings;
use spl_readings;

CREATE TABLE readings (value FLOAT(4,1), timestamp INT);
select * from readings;
insert into readings values(1, 2);

use mysql;
drop user 'grafana';
CREATE USER 'grafana' IDENTIFIED BY 'grafana';
GRANT SELECT ON spl_readings.readings TO 'grafana';

FLUSH PRIVILEGES;
```

## Credits  
Core part of this project (`splread.c`) is based on https://github.com/pvachon/gm1356.
