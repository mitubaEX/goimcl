# image crawler for twitter

## Start file server

```
mkdir Images

docker run -it -p 8000:8000 -v $PWD/Images:/app/public --name gohttpserver mitubaex/gohttp
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
