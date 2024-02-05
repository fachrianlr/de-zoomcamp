# Data Engineering Zoomcamp

The notes and exercises in this repository are a compilation from my participation in the Data Engineer Zoomcamp offered by Data Talks Club [Data Talks Club](https://github.com/DataTalksClub/data-engineering-zoomcamp).

## Content

Data source : [Yellow Taxi Data New York](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)


### 01 Docker-Terraform
* Navigate to the Docker-Terraform directory
```bash
cd de-zoomcamp/01
```
* Running Postgres & pgAdmin
```bash
chmod +x ./docker-compose.sh
./docker-compose.sh
```
* Ingesting data to Postgres
```bash
chmod +x ./ingest-run.sh
./ingest-run.sh
```
* Running Terraform Script
```bash
cd terraform/terraform_with_variable
terraform init
terraform plan
terraform apply
```