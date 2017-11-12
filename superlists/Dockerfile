# Run a django web server
FROM python:3.6
ENV WEBPATH /home/elspeth
RUN mkdir $WEBPATH
WORKDIR $WEBPATH
COPY requirements.txt $WEBPATH/
RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --no-cache-dir
COPY . /$WEBPATH/
CMD python3 manage.py migrate \
    && python3 manage.py runserver 0.0.0.0:8000

