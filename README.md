# Purser
EWallet API

## Run in docker

### Create docker network and docker volume
```bash
docker network create purser-net
```
```bash
docker volume create purser-data
```

### Run mysql container in the docker network and docker volume
```bash
docker run -d --network purser-net --network-alias mysql -v purser-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=purser mysql:5.7
```

### Run the django app on the domain `purser.iitsar.com` and specify a volume to serve media files
```bash
docker run -dp 8381:80 --network purser-net -v /home/iitsar/purser.iitsar.com:/app/media fshangala/purser:main
```

## Test in docker
```bash
docker run -dp 8000:80 -v /home/iitsar/sample.iitsar.com:/app/media fshangala/purser:dev
```

## Run Database migrations and create super user
```bash
docker exec -it <container_id> /bin/bash
```
```bash
python manage.py migrate
```
```bash
python manage.py createsuperuser --username admin --email admin@localhost
```