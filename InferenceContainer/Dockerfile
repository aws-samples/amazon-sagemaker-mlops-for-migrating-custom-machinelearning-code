# syntax=docker/dockerfile:experimental
# Define global args
ARG RUNTIME_VERSION="3.8"
ARG DISTRO_VERSION="buster"


#################################################
# Stage 1 - Create base image                   #
#################################################
FROM public.ecr.aws/docker/library/python:${RUNTIME_VERSION}-slim-${DISTRO_VERSION} AS python-slim

#RUN apt-get update && \
#    apt-get install -y gcc \
#    build-essential -y

# Upgrade pip and setup-tools
RUN pip install --upgrade pip && \
    pip install --upgrade setuptools


# Create code directory
# in theory code-dir can be changed but be warned ..
ARG CODE_DIR="/opt/ml/code/"
WORKDIR ${CODE_DIR}
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

# Install code dependencies
COPY ./src/requirements.txt ${CODE_DIR}

RUN pip3 install -r ${CODE_DIR}/requirements.txt

# copy all project scripts directly to CODE_DIR
# for easy :-) integration with sagemaker-training
COPY ./src/* ${CODE_DIR}
#RUN chmod a+x ${CODE_DIR}/*.sh

# default

CMD [ "python", "/opt/ml/code/predict.py"]
