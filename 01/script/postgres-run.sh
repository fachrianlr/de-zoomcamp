#!/bin/bash

docker build -t postgres-alpine:16 -f Dockerfile-postgres .

# Set environment variables
export POSTGRES_USER="zoomcamp"
export POSTGRES_PASSWORD="zoomcamp"
export POSTGRES_DB="ny_taxi"

# Run PostgreSQL container
docker run -d \
  --name de_zoomcamp \
  -e POSTGRES_USER="${POSTGRES_USER}" \
  -e POSTGRES_PASSWORD="${POSTGRES_PASSWORD}" \
  -e POSTGRES_DB="${POSTGRES_DB}" \
  -p 5432:5432 \
  postgres-alpine:16
