#! /bin/bash

sudo docker-compose down nginx dcb_frontend
git pull origin prod
sudo docker-compose --env-file .env.production up --build nginx dcb_frontend