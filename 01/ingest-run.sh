#!/bin/bash

#download green trip data
echo "==============start============="
file_url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz"
parent_folder="./data"
destination_folder="./data"
mkdir -p "$destination_folder"
filename=$(basename "$file_url")
destination_file="$destination_folder/$filename"

if [ -e "$destination_file" ]; then
    echo "File $filename already exists. Skipping download."
else
    echo "Download File..."
    curl -L -o "$destination_file" "$file_url"
fi

csv_file="$parent_folder/green_trip_data.csv"

echo "Extract file To: $csv_file"
gunzip -k -f "./$destination_file" -c > "$csv_file"
echo "==============end============="

echo "==============start============="
#download taxi+_zone_lookup data
file_url="https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv"
parent_folder="./data"
destination_folder="./data"
mkdir -p "$destination_folder"
filename=$(basename "$file_url")
destination_file="$destination_folder/$filename"

if [ -e "$destination_file" ]; then
    echo "File $filename already exists. Skipping download."
else
    echo "Download File..."
    curl -L -o "$destination_file" "$file_url"
fi

echo "rename file"
mv "./$destination_file" "$parent_folder/taxi_zone_lookup.csv"
echo "==============end============="


docker build -t python:3.9-alpine -f Dockerfile-ingest .
docker run -it --rm \
--network=01_zoomcamp \
python:3.9-alpine
