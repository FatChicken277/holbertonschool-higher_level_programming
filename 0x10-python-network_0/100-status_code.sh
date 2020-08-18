#!/bin/bash
# This script  displays only the status code of the response.
curl -sI "$1" | awk '/^HTTP/{print $2}'
