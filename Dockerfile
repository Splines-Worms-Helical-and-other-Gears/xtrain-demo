# -*- coding: utf-8 -*-
##################################################################################
# Launches the xtraindemo and writes some text to console, via the
# logging service.
#
# Authors: Hans Solo, Chewbacca
# Copyright (C) 2020, Teck Resources
# All rights reserved.
##################################################################################

# The alphine based OS keeps the distribution small.
FROM python:3-alpine

# Specify build version when creating the docker in the form TODO
ARG BUILD_VERSION
ENV PACKAGE_VERSION=$BUILD_VERSION

## Copy over local files for installation.
ENV PACKAGE pythonskeleton

RUN mkdir -p /pythonskeleton/pythonskeleton
COPY xtraindemo /pythonskeleton/pythonskeleton
COPY setup.py /pythonskeleton
COPY version /pythonskeleton
COPY README.md /pythonskeleton

### Install the package
RUN pip install pythonskeleton/
#
### Remove directory when done
RUN rm -rf /pythonskeleton
#
## Only the package name is needed since the entrypoint is defined in setup.py
# TODO, this currently fails in the main branch
# THIS IS A CHANGE MADE AND COMMITTED (BUT NOT PUSHED) IN THE MAIN BRANCH
# CMD ["xtraindemo"]

CMD ["/bin/sh"]