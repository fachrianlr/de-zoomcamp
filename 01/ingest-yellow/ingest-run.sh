#!/bin/bash


file_url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
parent_folder="./"
destination_folder="./data"
mkdir -p "$destination_folder"
filename=$(basename "$file_url")
destination_file="$destination_folder/$filename"

if [ -e "$destination_file" ]; then
    echo "File already exists. Skipping download."
else
    echo "Download File..."
    curl -L -o "$destination_file" "$file_url"
fi

csv_file="$parent_folder/data.csv"

echo "Extract file To: $csv_file"
gunzip -k -f "./$destination_file" -c > "$csv_file"

docker build -t python:3.9-alpine -f Dockerfile-ingest .

docker run -it --rm \
--network=01_zoomcamp \
python:3.9-alpine
