yellow='\033[1;33m'
no_color='\033[0m'

while true
do
    date >> "$0.log"
    printf "${yellow}starting splread${no_color}\n" >&2
    ./splread -f -r 30-80 -i 150 | tee >(nc -N localhost 2389)
    sleep 1
    printf "\n" >&2
done
