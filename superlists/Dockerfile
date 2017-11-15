# Run a django web server
FROM python:3.6
ENV WEBPATH /home/elspeth
WORKDIR $WEBPATH
COPY requirements.txt $WEBPATH/
RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --no-cache-dir
COPY . $WEBPATH/
EXPOSE 8000
CMD python3 manage.py migrate \
    && python3 manage.py runserver 0.0.0.0:8000
#ENTRYPOINT [docker-entrypoint.sh]

