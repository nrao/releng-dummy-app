FROM python:3.14-slim

WORKDIR /workspace

COPY pyproject.toml ./

RUN pip install --root-user-action=ignore --no-cache-dir --upgrade pip pip-tools && \
    pip install --root-user-action=ignore --no-cache-dir --group test

COPY pytest.ini tests/ ./

ENV PYTHONPATH="/workspace"
ENV TEST_BASE_URL="http://dummy-app:5000"

ENTRYPOINT [ "python", "-m", "pytest" ]
CMD [ "smoke" ]
