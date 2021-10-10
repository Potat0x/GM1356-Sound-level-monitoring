echo "creating datasource"
curl -o - -u admin:admin --header "Content-Type: application/json" -X POST http://127.0.0.1:13000/api/datasources -d @datasource.json
# curl -u admin:admin http://127.0.0.1:13000/api/datasources

echo "creating dashboard"
curl -o - -u admin:admin --header "Content-Type: application/json" -X POST http://127.0.0.1:13000/api/dashboards/db -d @dashboard.json
