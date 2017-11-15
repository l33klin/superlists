# Run a django web server
FROM python:3.6
ENV WEBPATH /usr/src/app
WORKDIR $WEBPATH
COPY . $WEBPATH/
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --no-cache-dir
EXPOSE 8000
CMD python3 manage.py migrate \
    && python3 manage.py runserver 0.0.0.0:8000
#ENTRYPOINT [docker-entrypoint.sh]

