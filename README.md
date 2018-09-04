# image crawler for twitter

## Start file server

```
mkdir Images

docker run -it -p 8000:8000 -v $PWDImages:/app/public --name gohttpserver -v '/etc/ssl/certs/ca-certificates.crt:/etc/ssl/c
erts/ca-certificates.crt' -e ACCESS_TOKEN='' -e ACCESS_TOKEN_SECRET=''
 -e CONSUMER_KEY='' -e CONSUMER_SECRET='' mitubaex/gohttp
```

## Setup your twitter token

open setup.sh and write your twitter token

```
export CONSUMER_KEY=<Your Token>
export CONSUMER_SECRET=<Your Token>
export ACCESS_TOKEN=<Your Token>
export ACCESS_TOKEN_SECRET=<Your Token>
```

## Start crawler

```
sh setup.sh
```

Please access to [http://localhost:8000](http://localhost:8000)
