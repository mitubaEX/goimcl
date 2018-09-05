# image crawler for twitter

## Start file server

```
mkdir Images

docker run -it -p 8000:8000 -v $PWD/Images:/app/public --name gohttpserver -v '/etc/ssl/certs/ca-certificates.crt:/etc/ssl/certs/ca-certificates.crt' -e "ACCESS_TOKEN=" -e "ACCESS_TOKEN_SECRET=" -e "CONSUMER_KEY=" -e "CONSUMER_SECRET=" mitubaex/gohttp
```

## Start crawler

```
docker run -it -v $PWD/Images:/app/Images --name craw -v '/etc/ssl/certs/ca-certificates.crt:/etc/ssl/certs/ca-certificates.crt' -e "ACCESS_TOKEN=" -e "ACCESS_TOKEN_SECRET=" -e "CONSUMER_KEY=" -e "CONSUMER_SECRET=" mitubaex/craw
```

Please access to [http://localhost:8000](http://localhost:8000)
