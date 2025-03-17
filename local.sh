#!/bin/bash

docker build -t server .
docker run \
    -e APP_ENV=development \
    -p 8085:8085 \
    -v  $(pwd)/server:/server \
    -it \
    --env-file ./server/.env server
