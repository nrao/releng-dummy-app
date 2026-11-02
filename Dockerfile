FROM python:3.14-slim

LABEL org.opencontainers.image.title="NRAO Release Engineering Dummy App"
LABEL org.opencontainers.image.description="A minimal app for testing and demoing GitOps processes"
LABEL org.opencontainers.image.vendor="Associated Universities, Inc. Washington DC, USA"
LABEL org.opencontainers.image.url="https://public.nrao.edu/"
LABEL org.opencontainers.image.licenses="BSD-3-Clause"
LABEL org.opencontainers.image.source="https://github.com/nrao/dummy-app" 

WORKDIR /app

COPY pyproject.toml ./

RUN pip install --root-user-action=ignore --no-cache-dir --upgrade pip pip-tools && \
    pip-compile pyproject.toml --output-file requirements.txt && \
    pip install --root-user-action=ignore --no-cache-dir -r requirements.txt

COPY src/ ./

ARG VERSION
ENV VERSION=$VERSION
ENV SETUPTOOLS_SCM_PRETEND_VERSION_FOR_DUMMY_APP=$VERSION

RUN pip install --root-user-action=ignore --no-cache-dir .

COPY container/ ./

ENV PYTHONPATH="/app"

ENV SAMPLE_VAR=docker_default
ENV COLOR=blue
ENV CONTEXT_PATH=/

EXPOSE 5000

CMD [ "python", "standalone.py"]
