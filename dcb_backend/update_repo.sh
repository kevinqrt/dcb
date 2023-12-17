#! /bin/bash

sudo docker-compose down
git pull origin prod
sudo docker-compose --env-file ./.env.production up --build nginx dcb_backend database redis