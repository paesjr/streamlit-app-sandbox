FROM python:3.10-buster

ARG GITLAB_TOKEN

RUN apt update && apt install -y gdal-bin gdal-data libgdal-dev libsnappy-dev gfortran

ADD requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

ADD . /app
ADD .streamlit/config.toml /root/.streamlit/config.toml

# Streamlit JS patch to workaround an issue preventing the app to work on low latency networks
# Issue Ref: https://github.com/streamlit/streamlit/issues/2312
RUN sed -i -e 's/),1e3)/),1e4)/g' /usr/local/lib/python3.10/site-packages/streamlit/static/static/js/main.*.js
RUN sed -i -e 's/baseUriPartsList,500/baseUriPartsList,10000/g' /usr/local/lib/python3.10/site-packages/streamlit/static/static/js/main.*.js

WORKDIR /app

