#!/bin/bash

set -e

echo "Updating repository"

cd /opt/python-service

git pull origin main

echo "Rebuilding containers"

docker compose up -d --build

echo "Deployment finished"