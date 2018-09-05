FROM python

ADD . /app
WORKDIR /app

RUN mkdir -p /app/Images && pip3 install -r ./requirements.txt
VOLUME /app/Images

CMD ["sh", "./setup.sh"]
