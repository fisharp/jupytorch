# Base image tag
ARG python=python:3.10-slim

# -- Base python image with NodeJS
FROM ${python} AS base
RUN apt update \
    && \
    apt install -y \
        curl    \
        wget    \
        vim     \
        git     \
    && \
    apt clean


# -- Build Wheels first
FROM base AS build

ENV CORE_DL_LIB_REQS        packages/core-dl-libs/requirements.txt
ENV JUPYTER_SERVER_REQS     packages/jupyter-server/requirements.txt
ENV SERVER_EXTENSIONS_REQS  packages/server-extensions/requirements.txt
# ENV JUPYTER_LAB_EXTENSIONS  packages/node-extensions/jupyterlab-extensions.ini

ENV WHEELS_TMP_DIR  /tmp/wheels
ENV WORK_SPACE_DIR  /tmp/source

WORKDIR ${WORK_SPACE_DIR}

# Creating the virtual env to work on
RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:${PATH}

# This will be run within the venv python from now on
RUN python -m pip install --upgrade pip && \
    python -m pip install --upgrade wheel cleanpy

COPY ${CORE_DL_LIB_REQS} \
        core-dl-lib.reqs

RUN python -m pip wheel \
    --wheel-dir=${WHEELS_TMP_DIR} \
    -r core-dl-lib.reqs

COPY ${JUPYTER_SERVER_REQS} \
        jupyter-server.reqs

RUN python -m pip wheel \
    --wheel-dir=${WHEELS_TMP_DIR} \
    -r jupyter-server.reqs


# -- Install directly from pre-built wheels
FROM build AS install

# Install main packages from Wheels cache
RUN python -m pip install --no-index    \
        --find-links=${WHEELS_TMP_DIR}  \
        -r core-dl-lib.reqs             \
        -r jupyter-server.reqs

COPY ${SERVER_EXTENSIONS_REQS} \
        server-extensions.reqs

# Now including extras and server extensions
# directly from main pipy repository
# Main packages included again to guarantee version boundaries
RUN python -m pip install \
        -r server-extensions.reqs  \
        -r jupyter-server.reqs     \
        -r core-dl-lib.reqs

ENTRYPOINT /bin/bash


# -- Cleaning stage to reduce final size
FROM install AS clean

RUN cleanpy /opt/venv && \
    python -m pip cache purge


# -- Final stage
FROM base AS final

ARG BUILD_DATE

ARG USER=jupyter
ARG UID=1000
ARG GID=1000

LABEL org.label-schema.name="JuPyTorch"
LABEL org.label-schema.description="JupyterLab based data science workspace using PyTorch with NVIDIA® CUDA® GPU support"
LABEL maintainer "Hector Salvador (Fisharp) <fisharp.git@gmail.com>"
LABEL org.opencontainers.image.authors="Hector Salvador (Fisharp) <fisharp.git@gmail.com>"
LABEL org.opencontainers.image.source="https://github.com/fisharp/jupytorch"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.label-schema.build-date=${BUILD_DATE}
LABEL org.label-schema.schema-version="1.0"

ENV VARDATA /var/data
ENV PATH    /opt/venv/bin:${PATH}
ENV SHELL   /bin/bash

ENV JUPYTER_CONFIG_DIR  /var/config

RUN groupadd -g ${GID} ${USER} && \
    useradd  -u ${UID} -g ${USER} -m ${USER} && \
    mkdir -p ${VARDATA} && \
    chmod 777 ${VARDATA}

WORKDIR ${VARDATA}

COPY --chown=${USER} --from=clean /opt/venv /opt/venv
COPY --chown=${USER} --chmod=755 entrypoint.py /opt/venv/bin/entrypoint
COPY --chown=${USER} config/default.py ${JUPYTER_CONFIG_DIR}/jupyter_lab_config.py
COPY --chown=${USER} config/overrides.json /opt/venv/share/jupyter/lab/settings/overrides.json

USER ${USER}

VOLUME ${VARDATA}
EXPOSE 8888

ENTRYPOINT ["entrypoint"]
CMD ["jupyter", "lab"]
