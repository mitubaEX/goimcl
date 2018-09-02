#coding: UTF-8
from requests_oauthlib import OAuth1Session
import json
import requests
import sys
import urllib
import os.path
import time
import sys
import os

twitter = OAuth1Session(os.environ["CONSUMER_KEY"],
                        os.environ["CONSUMER_SECRET"],
                        os.environ["ACCESS_TOKEN"],
                        os.environ["ACCESS_TOKEN_SECRET"]
                        )
# 別ファイルtwitkey.pyから必要な各パラメータ値を参照します。

Get_Count = 50  # Get_Countにツイートの取得回数を指定
Get_At_Once = 200  # Get_At_Onceに1回の取得で遡るツイートの数を指定
User_Id = sys.argv[1]  # User_Idに画像を遡りたいユーザのidを指定 例:github
Path = "./Images/"  # Pathに画像を保存したいディレクトリのファイルパスを指定してください　例:./Images/

for i in range(1, Get_Count):
    if(i == 1):
        params = {"count": Get_At_Once}
    else:
        params = {"count": Get_At_Once, "max_id": num}
    req = twitter.get("https://api.twitter.com/"
                      "1.1/statuses/user_timeline.json"
                      "?screen_name=%s&include_rts=false" % User_Id,
                      params=params)
    timeline = json.loads(req.text)
    if(req.status_code == 200):
        if(i == 1):
            counter = 1
        else:
            counter = count
        for tweet in timeline:
            num = tweet["id"]
            counter = counter+1

            import re

            mlist = re.findall('#[a-zA-Z1-9]+', tweet['text'])
            if len(mlist) == 0:
                continue

            if("extended_entities" in tweet.keys()):
                if("media" in tweet["extended_entities"].keys()):
                    for i in range(0, len(tweet["extended_entities"]["media"])):
                        if("type" in tweet["extended_entities"]["media"][i].keys()):
                            if(tweet["extended_entities"]["media"][i]["type"] == "photo"):

                                url = tweet["extended_entities"]["media"][i]["media_url_https"]
                                img = urllib.request.urlopen(url)
                                Name = tweet["user"]["name"]
                                created_at = tweet["created_at"]
                                Month = created_at[4:7]
                                Date = created_at[8:10]
                                Hour = created_at[11:13]
                                Minute = created_at[14:16]
                                Second = created_at[17:19]
                                Year = created_at[26:]
                                img_name = Year+"_"+Month+"_"+Date+"_"+Hour+"_"+Minute+"_"+Second

                                hsashtag_path = '_'.join(mlist)
                                os.makedirs(Path + hsashtag_path,
                                            exist_ok=True)

                                localfile = open(
                                    Path + hsashtag_path + "/" + img_name + "_"+str(i)+".jpg", 'wb')
                                localfile.write(img.read())
                                img.close()
                                localfile.close()
            else:
                print("No Image")
        count = counter
    else:
        print(req.status_code)
        time.sleep(240)
        # エラー処理
