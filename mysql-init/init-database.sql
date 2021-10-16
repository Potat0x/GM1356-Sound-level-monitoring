CREATE DATABASE gm1356_monitoring;
USE gm1356_monitoring;
CREATE TABLE readings (_value FLOAT(4,1), _timestamp INT);


CREATE USER 'grafana'@'%' IDENTIFIED BY 'grafana';
GRANT SELECT ON gm1356_monitoring.* TO 'grafana'@'%';

FLUSH PRIVILEGES;
