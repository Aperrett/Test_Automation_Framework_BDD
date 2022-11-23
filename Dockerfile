FROM python:3.11.0-alpine3.16

WORKDIR /taf

COPY . .

RUN apk add --update --no-cache chromium g++ gcc libxslt-dev ttf-dejavu \
    ttf-liberation tzdata libffi-dev chromium-chromedriver \
    && chmod -R 777 /taf \
    && pip install --upgrade pip --no-cache-dir -r requirements.txt \
    && mkdir reports screenshots

ENV PYTHONPATH /taf/lib TAF_CI True TZ Europe/London 

ENTRYPOINT ["behave"]

CMD ["/bin/sh"]