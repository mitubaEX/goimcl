export CONSUMER_KEY=<Your Token>
export CONSUMER_SECRET=<Your Token>
export ACCESS_TOKEN=<Your Token>
export ACCESS_TOKEN_SECRET=<Your Token>

mkdir Images

for userID in Story_terrorV2 satake_take
do
  python3 imgcrawler.py "$userID"
done
