echo "The script you are running has basename `basename "$0"`, dirname `dirname "$0"`"
API_URL="http://localhost:13000/api"
printf "create datasource\n"
curl -o - -d @datasource.json -w "\n%{response_code}\n" -X POST $API_URL/datasources -u admin:admin -H "Content-Type: application/json"

printf "\ncreate dashboard\n"
curl -o -  -d @dashboard.json -w "\n%{response_code}\n" -X POST $API_URL/dashboards/db -u admin:admin -H "Content-Type: application/json"

printf "\n"
