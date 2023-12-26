#! /bin/bash

sudo docker-compose down nginx dcb_frontend
git pull origin prod
sudo docker-compose up --build nginx dcb_frontend