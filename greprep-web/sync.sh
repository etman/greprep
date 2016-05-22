CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

while true; do
	mv /tmp/sync.log /tmp/sync.last 2>/dev/null; rsync -rcv ${CURRENT_DIR}/src/* ${CURRENT_DIR}/online/greprep-1319/ | tee /tmp/sync.log | diff /tmp/sync.last -
	sleep 2
done
