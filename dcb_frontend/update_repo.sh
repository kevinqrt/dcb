#! /bin/bash

sudo docker-compose down
git pull origin prod
sudo docker-compose up --build