FROM python:3.6.8-slim

WORKDIR /opt/app

# Create output directory as its expected
RUN mkdir output

# Upgrade pip and setuptools
RUN pip install -U pip==19.2.3 setuptools==41.2.0

# First copy scripts and setup.py to install dependencies
# and avoid reinstalling dependencies when only changing the code
COPY setup.py setup.py
COPY scripts scripts

# Install only install_requires as well as tensorflow without executing
# the cmdclass "develop"
ARG TF_VARIANT=cpu
RUN pip install $(./scripts/get_requires_from_setup.py $TF_VARIANT)

COPY xain xain
COPY protobuf protobuf

RUN pip install -e .
