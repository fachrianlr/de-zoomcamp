docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

# Remove all images
docker rmi $(docker images -a -q)

# Stop and remove all containers
docker volume ls -q | xargs docker volume rm