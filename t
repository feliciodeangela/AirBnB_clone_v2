#!/usr/bin/env bash
# Transfer file from the client to a server
# Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
if [ $# -ge 4 ]; then
    scp -o StrictHostKeyChecking=no -i "$4" "$1" "$3"@"$2":'~/'
else
    echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
fi
