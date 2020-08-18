#!/use/bin/env bash
# This script sends a request to a URL, and displays the
# size of the body of the response.

if [ "$#" -eq 1 ]; then
    curl -sI "$1" | awk -v Del=": " '/^Content-Length/{print $2}'
fi
