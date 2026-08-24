FROM python:3.13-slim-trixie AS builder

WORKDIR /workspace

COPY pyproject.toml ./

RUN pip install --root-user-action=ignore --no-cache-dir --upgrade pip==26.2.1 pip-tools==7.6.1 && \
    pip install --root-user-action=ignore --no-cache-dir --group test --target /packages

FROM gcr.io/distroless/python3-debian13

WORKDIR /workspace

COPY --from=builder /packages /packages

COPY tests/ ./

ENV PYTHONPATH="/packages:/workspace"
ENV TEST_BASE_URL="http://dummy-app:5000"

ENTRYPOINT [ "/usr/bin/python", "-m", "pytest" ]
CMD [ "smoke"]
