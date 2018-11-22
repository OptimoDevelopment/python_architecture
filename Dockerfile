# Base build image with dependencies
FROM python:3.7.0-alpine3.8 as dependencies

RUN apk --no-cache add bash

ARG PACKAGE_VERSION=0.0.1+docker
ARG SRC=/opt/app

ENV SETUPTOOLS_SCM_PRETEND_VERSION ${PACKAGE_VERSION}
ENV PBR_VERSION ${PACKAGE_VERSION}

ADD . ${SRC}

RUN pip install ${SRC}/shop
RUN pip install ${SRC}/ram_db
RUN pip install ${SRC}/api

EXPOSE 8080

ENTRYPOINT ["shop-api"]